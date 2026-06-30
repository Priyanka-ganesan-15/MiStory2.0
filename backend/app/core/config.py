from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./mistory.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
