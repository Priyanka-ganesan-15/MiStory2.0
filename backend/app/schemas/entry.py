from pydantic import BaseModel
from typing import Optional

class EntryRequest(BaseModel):
    patient_id: int
    text: str
    date: Optional[str] = None