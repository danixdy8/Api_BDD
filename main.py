from fastapi import FastAPI
import models 
from db import create_all_tables
from routes import users

app = FastAPI(
    title="API EC2 y RDS",
    lifespan=create_all_tables
)

app.include_router(users)

@app.get("/")
def raiz():
    return {"estado": "API operativa", "docs": "/docs"}
