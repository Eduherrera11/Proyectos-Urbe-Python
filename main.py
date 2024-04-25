from fastapi import FastAPI
from routes.authors import authors_routes
from routes.books import books_routes

app = FastAPI()

app.title = "Proyecto 04"
app.description = "Backend gestor de libreria en FastApi"
app.version = "1.0.0"

# Pasamos las rutas de nuestos metodos a la app
app.include_router(books_routes)
app.include_router(authors_routes)

# comando para iniciar la api
# uvicorn main:app --reload 