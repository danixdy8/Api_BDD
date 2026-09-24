from fastapi import APIRouter, HTTPException
from typing import List
from sqlmodel import select
from models import Usuario, Libro
from db import SessionDep

users = APIRouter(prefix="/usuarios", tags=["usuarios"])
libros = APIRouter(prefix="/libros", tags=["libros"])

@users.post("/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: SessionDep):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@users.get("/", response_model=List[Usuario])
def listar_usuarios(session: SessionDep):
    return session.exec(select(Usuario)).all()

@users.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@users.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, datos: Usuario, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombre = datos.nombre
    usuario.email = datos.email
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@users.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(usuario)
    session.commit()
    return {"ok": True}

@libros.post("/", response_model=Libro)
def crear_libro(libro: Libro, session: SessionDep):
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

@libros.get("/", response_model=List[Libro])
def listar_libros(session: SessionDep):
    return session.exec(select(Libro)).all()

@libros.get("/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@libros.put("/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: int, datos: Libro, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    libro.titulo = datos.titulo
    libro.autor = datos.autor
    libro.usuario_id = datos.usuario_id
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

@libros.delete("/{libro_id}")
def eliminar_libro(libro_id: int, session: SessionDep):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    session.delete(libro)
    session.commit()
    return {"ok": True}
