from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from json import load


authors_routes = APIRouter()

# Mediante un metodo get obtenemos todos los autores
@authors_routes.get("/authors", tags=["Obtener Autores"])
async def get_authors():
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        data = load(jsonfile)
        autores = data["authors"]

        return JSONResponse(content=autores, status_code=status.HTTP_200_OK)

# Mediante un metodo get y una condicional que hacede a los id obtenemos un autor por su id 
@authors_routes.get("/authors/{id}", tags=["Obtener Autor"])
async def get_author(id: str):
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        data = load(jsonfile)
        autores = data["authors"]

    for autor in autores:
        if autor["id"] == id:
            return JSONResponse(content=autor, status_code=status.HTTP_200_OK)
        