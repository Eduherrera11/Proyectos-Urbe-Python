from pydantic import BaseModel, Field
from typing import Optional
import uuid


#Clases de validacion
class Author(BaseModel):
    id: str = str(uuid.uuid1())
    fullname: str = Field(min_length=5, max_length=45)
    date_birth: str 


     # Ejemplo de resquet
    model_config = {
        "json_schema_extra": {
                "authors":
                    [{
                    "id": "177ec-8d3d-024238d3c-9f1e-11ac130003",
                    "fullname": "Eduardo Herrera",
                    "date_birth": "08-12-2003"
                    }]
        }
    }