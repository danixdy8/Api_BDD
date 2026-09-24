from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class UsuarioBase(SQLModel):
    nombre: str
    email: str = Field(unique=True, index=True)

class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    libros: List["Libro"] = Relationship(back_populates="usuario")

class LibroBase(SQLModel):
    titulo: str
    autor: str
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")

class Libro(LibroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario: Optional[Usuario] = Relationship(back_populates="libros")