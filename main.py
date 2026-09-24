from fastapi import FastAPI
import models 
from db import create_db_and_tables
from routes import users, libros

app = FastAPI(
    title="API EC2 y RDS",
    lifespan=create_db_and_tables
)

app.include_router(users)
app.include_router(libros)

@app.get("/")
def raiz():
    return {"estado": "API operativa", "docs": "/docs"}
