from fastapi import APIRouter
from pydantic import BaseModel

from app.services.copilot_rag import ask_copilot

router = APIRouter()


class CopilotRequest(BaseModel):
    patient_id: int
    question: str


@router.post("/copilot/ask")
def copilot_ask(payload: CopilotRequest):

    result = ask_copilot(payload.patient_id, payload.question)

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }