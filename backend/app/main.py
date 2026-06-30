from fastapi import FastAPI
from sqlmodel import SQLModel

from app.core.config import engine
from app.api.routes.entry import router as entry_router
from app.api.routes.patient import router as patient_router
from app.api.routes.copilot import router as copilot_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MiStory Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLModel.metadata.create_all(engine)

app.include_router(entry_router, prefix="/api")
app.include_router(patient_router, prefix="/api")
app.include_router(copilot_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "MiStory Backend Running 🚀"}