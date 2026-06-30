from fastapi import APIRouter
from sqlmodel import Session
from datetime import datetime

from app.core.config import engine
from app.models.entry import Entry
from app.schemas.entry import EntryRequest

from app.services.extractor import extract_symptoms
from app.services.vector_store import add_entry

router = APIRouter()


@router.post("/entry")
def create_entry(payload: EntryRequest):

    # 1. AI extraction (BERT pipeline)
    extracted = extract_symptoms(payload.text)

    # 2. NORMALIZE symptoms (CRITICAL FIX)
    normalized_symptoms = []

    for s in extracted.get("symptoms", []):
        if isinstance(s, dict):
            normalized_symptoms.append({
                "name": s.get("name", "unknown"),
                "confidence": float(s.get("confidence", 0))
            })
        else:
            normalized_symptoms.append({
                "name": str(s),
                "confidence": 0.5
            })

    # 3. Store structured entry in DB
    entry = Entry(
        patient_id=payload.patient_id,
        raw_text=payload.text,
        symptoms=normalized_symptoms,   # 🔥 FIX: NO json.dumps
        body_system=extracted.get("body_system", "General"),
        severity=extracted.get("severity", "low"),
    )

    with Session(engine) as session:
        session.add(entry)
        session.commit()
        session.refresh(entry)

    # 4. RAG memory (ENHANCED — FIX)
    add_entry(
        entry_id=entry.id,
        text=f"""
        TEXT: {payload.text}
        SYMPTOMS: {normalized_symptoms}
        SYSTEM: {entry.body_system}
        SEVERITY: {entry.severity}
        """
    )

    # 5. Response (frontend-safe)
    return {
        "entry": {
            "id": entry.id,
            "patient_id": entry.patient_id,
            "raw_text": entry.raw_text,
            "symptoms": normalized_symptoms,
            "body_system": entry.body_system,
            "severity": entry.severity,
            "created_at": entry.created_at
        },
        "ai_extraction": extracted
    }