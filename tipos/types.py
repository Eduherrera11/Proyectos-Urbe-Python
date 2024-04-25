from typing import List, Dict, Union

# Tipado de datos
AuthorType = Dict[str, str]
AuthorsType = List[AuthorType]

BookType = Dict[str, Union[str, int, List[AuthorType]]]
BooksType = List[BookType]

DatabaseType = Dict[str, Union[BooksType, AuthorsType]]
