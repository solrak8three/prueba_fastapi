from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hola desde /"}

@router.get("/saludo")
def saludo():
    return {"saludo": "¡Hola Solrak83, esto funciona!"}

@router.get("/status")
def status():
    return {"status": "ok", "servidor": "Clouding", "deploy": "GitHub Actions"}
