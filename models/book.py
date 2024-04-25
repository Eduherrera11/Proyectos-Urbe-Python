from pydantic import BaseModel, Field
from typing import Optional
import uuid
from models.author import Author


#Clases de validacion

class Book(BaseModel):
    id: str = str(uuid.uuid1())
    title: str = Field(min_length=5, max_length=20)
    category: str = Field(min_length=5, max_length=10)
    release_date: int
    authors: list[Author]

    # Ejemplo de resquet
    model_config = {
        "json_schema_extra": {
            "book_example": {
                "id": "1773-11ec-8d3d-0248d3c-9f1e2ac130004",
                "title": "Machine learning",
                "category": "Ficcion",
                "release_date": 2024,
                "authors": [
                    {
                    "id": "177ec-8d3d-024238d3c-9f1e-11ac130003",
                    "fullname": "Eduardo Herrera",
                    "date_birth": "08-12-2003"
                    },
                    {
                    "id": "177ec-8d3d8d3c-9f1e-11ac1300-0242303",
                    "fullname": "Kelly Herrera",
                    "date_birth": "08-01-2004"
                    },
                    {
                    "id": "17-024238d3c-9f1e-11a7ec-8d3dc130003",
                    "fullname": "Jesus Duque",
                    "date_birth": "08-11-2003"
                    }
                ] 
            }
        }
    }

