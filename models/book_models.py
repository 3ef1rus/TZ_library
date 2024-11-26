from typing import Optional, Union
import uuid


class Book:

    def __init__(
            self,
            title: str,
            author: str,
            year: int,
            id: Optional[Union[uuid.UUID, str]] = None,
            status: Optional[bool] = None
    ) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

        if id is None:
            self.id: Union[uuid.UUID, str] = uuid.uuid4().hex
        else:
            self.id = id
        if status is None:
            self.status: bool = True
        else:
            self.status = status

    def show_book(self) -> None:
        status = "В наличии" if self.status is True else "Выдана"
        print(f"id книги: {self.id},"
              f" Название книги: {self.title},"
              f" Автор книги: {self.author},"
              f" Год издания: {self.year},"
              f" Состояние книги: {status}")

    def change_status(self, status: bool) -> None:
        self.status = status
