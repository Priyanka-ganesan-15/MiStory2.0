from sqlmodel import SQLModel, Field
from datetime import datetime

class Entry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    patient_id: int
    raw_text: str

    symptoms: str
    body_system: str
    severity: str

    created_at: datetime = Field(default_factory=datetime.utcnow)