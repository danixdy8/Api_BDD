from fastapi import FastAPI
import models 
from database import create_db_and_tables
from routers import usuarios, libros

app = FastAPI(
    title="API de Gestión con EC2 y RDS", 
    lifespan=create_db_and_tables
)

app.include_router(usuarios.router)
app.include_router(libros.router)

@app.get("/")
def raiz():
    return {"estado": "API operativa", "documentacion": "/docs"}