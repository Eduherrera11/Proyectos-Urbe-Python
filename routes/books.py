from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.book import Book
from models.author import Author
from json import load, dump
from operator import itemgetter
from tipos.types import BooksType, BookType, AuthorsType, AuthorType, DatabaseType
from typing import cast



books_routes = APIRouter()

# Funcion para obtener el json de todos los libros
@books_routes.get("/books", tags=["Obtener libros"])
async def get_books():
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        data = load(jsonfile)
        books = data["books"]

        return JSONResponse(content=books, status_code=status.HTTP_200_OK)
    
# Funcion para obtener un libro por su id
@books_routes.get("/book/{id}", tags=["Obtener libro por id"])
async def get_book(id: str):
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        data = load(jsonfile)
        books = data["books"]

        for book in books:
            if book["id"] == id:
                return JSONResponse(content=book, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"error": "el id que ingresaste no existe."}, status_code=status.HTTP_404_NOT_FOUND)
    
@books_routes.get("/books/title/", tags=["Obtener libro por titulo"])
async def get_book_title(title: str):
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        data = load(jsonfile)
        books = data["books"]
        for book in books:
            if book["title"] == title:
                return JSONResponse(content=book, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"error": "el id que ingresaste no existe."}, status_code=status.HTTP_404_NOT_FOUND)

@books_routes.post("/books/", tags=["Agregar libro a la db"])
async def create_book(book: Book):
    
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        datos: DatabaseType = load(jsonfile)
        authors: AuthorsType = cast(AuthorsType, datos['authors'])
        datos_authors = []

        if len(book.authors) > 0:
            for book_author_id in book.authors:
                found = False
                for author in authors:
                    if author["id"] == book_author_id.id:
                        datos_authors.append(author)
                        found = True
                        break  # Detiene el bucle una vez que el autor es encontrado
                if not found:
                    return JSONResponse(content={"error": f"Autor no encontrado con ID: {book_author_id}"}, status_code=status.HTTP_400_BAD_REQUEST)


            if len(book.authors) == len(datos_authors):
                new_book = {
                                'id': book.id,
                                'title': book.title,
                                'category': book.category,
                                'release_date': book.release_date,
                                'authors': datos_authors
                            }

                datos['books'].append(new_book)

                with open("db-proyecto.json", "w", encoding="UTF-8") as new_jsonfile:
                    dump(datos, new_jsonfile, indent=2, ensure_ascii=False)

                return JSONResponse(content="Libro creado con exito.", status_code=status.HTTP_201_CREATED)
            

        else:
            return JSONResponse(content={"error": "no ingresaste ningun autor"}, status_code=status.HTTP_400_BAD_REQUEST)
        
 
    

@books_routes.put("/books/{id}", tags=["Actualizar Libro"])
async def update_book(id: str, book: Book):
    with open("db-proyecto.json", "r", encoding="UTF-8") as jsonfile:
        datos: DatabaseType = load(jsonfile)
        authors: AuthorsType = cast(AuthorsType, datos['authors'])
        books: BooksType = cast(BooksType, datos['books'])
        datos_authors = []

        if len(book.authors) > 0:
            for book_author_id in book.authors:
                found = False
                for author in authors:
                    if author["id"] == book_author_id.id:
                        datos_authors.append(author)
                        found = True
                        break  # Detiene el bucle una vez que el autor es encontrado
                if not found:
                    return JSONResponse(content={"error": f"ID no encontrado: {book_author_id}"}, status_code=status.HTTP_400_BAD_REQUEST)


            if len(book.authors) == len(datos_authors):
                update_book = {
                                'id': id,
                                'title': book.title,
                                'category': book.category,
                                'release_date': book.release_date,
                                'authors': datos_authors
                            }

                for index, current_book in enumerate(books):
                    if current_book['id'] == id:
                        books[index] = update_book

                with open("db-proyecto.json", "w", encoding="UTF-8") as new_jsonfile:
                    dump(datos, new_jsonfile, indent=2, ensure_ascii=False)

                return JSONResponse(content="Libro creado con exito.", status_code=status.HTTP_201_CREATED)
            

        else:
            return JSONResponse(content={"error": "no ingresaste ningun autor"}, status_code=status.HTTP_400_BAD_REQUEST)

@books_routes.delete("/books/{id}", tags=['Eliminar libros'])
async def delete_book(id: str):
    with open("db-proyecto.json", 'r', encoding="UTF-8") as jsonfile:
        datos: DatabaseType = load(jsonfile)
        books: BooksType = cast(BooksType, datos['books'])

    found = False
    for index, current_book in enumerate(books):
        if current_book['id'] == id:
            del books[index]
            found = True
            break

    if not found:
        return JSONResponse(content={"error": f"ID no encontrado: {id}"}, status_code=status.HTTP_404_NOT_FOUND)

    with open("db-proyecto.json", 'w', encoding="UTF-8") as new_jsonfile:
        dump(datos, new_jsonfile, indent=2, ensure_ascii=False)

    return JSONResponse(content="El Libro se ha eliminado.", status_code=status.HTTP_200_OK)

            
        


