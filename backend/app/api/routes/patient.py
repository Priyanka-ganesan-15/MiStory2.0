from fastapi import APIRouter
from app.services.patient_context import get_patient_history, build_patient_context

router = APIRouter()


@router.get("/patient/history/{patient_id}")
def patient_history(patient_id: int):
    return {
        "patient_id": patient_id,
        "history": get_patient_history(patient_id)
    }


@router.get("/patient/context/{patient_id}")
def patient_context(patient_id: int):
    return build_patient_context(patient_id)