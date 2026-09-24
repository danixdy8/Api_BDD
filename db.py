import os
import os
from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT", "5432")
NAME = os.getenv("DB_NAME")

rds_connection_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?sslmode=require"
engine = create_engine(rds_connection_string, echo=False)

def create_db_and_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
