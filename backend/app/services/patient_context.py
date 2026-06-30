from sqlmodel import Session, select
from app.core.config import engine
from app.models.entry import Entry
import json


def get_patient_history(patient_id: int):
    with Session(engine) as session:
        stmt = select(Entry).where(Entry.patient_id == patient_id)
        results = session.exec(stmt).all()

    history = []

    for r in results:
        history.append({
            "id": r.id,
            "text": r.raw_text,
            "symptoms": json.loads(r.symptoms),
            "body_system": r.body_system,
            "severity": r.severity,
            "created_at": r.created_at
        })

    return history


def build_patient_context(patient_id: int):
    history = get_patient_history(patient_id)

    all_symptoms = []
    system_count = {}
    severity_count = {"low": 0, "medium": 0, "high": 0}

    for h in history:
        for s in h["symptoms"]:
            # handle both string + dict formats
            if isinstance(s, dict):
                all_symptoms.append(s["name"])
            else:
                all_symptoms.append(s)

        system = h["body_system"]
        system_count[system] = system_count.get(system, 0) + 1

        severity_count[h["severity"]] += 1

    # most common system
    dominant_system = (
        max(system_count, key=system_count.get)
        if system_count else None
    )

    return {
        "patient_id": patient_id,
        "total_entries": len(history),
        "symptoms": all_symptoms,
        "system_distribution": system_count,
        "severity_distribution": severity_count,
        "dominant_system": dominant_system,
        "raw_history": history
    }