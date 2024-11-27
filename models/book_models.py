from typing import Optional, Union
import uuid


class Book:
    """
   Представляет книгу в библиотеке.

   Атрибуты:
       title (str): Название книги.
       author (str): Автор книги.
       year (int): Год издания книги.
       id (Union[uuid.UUID, str]): Уникальный идентификатор книги
                                   (генерируется автоматически, если не указан).
       status (bool, optional): Статус книги (True - в наличии, False - выдана).
                                 По умолчанию True.
    """

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
        """
        Отображает информацию о книге.

        Печатает на консоль следующую информацию:
            * id книги
            * Название книги
            * Автор книги
            * Год издания
            * Состояние книги (в наличии или выдана)
        """
        status = "В наличии" if self.status is True else "Выдана"
        print(f"id книги: {self.id},"
              f" Название книги: {self.title},"
              f" Автор книги: {self.author},"
              f" Год издания: {self.year},"
              f" Состояние книги: {status}")

    def change_status(self, status: bool) -> None:
        """
       Изменяет статус книги (в наличии/выдана).

       Args:
           status (bool): Новый статус книги (True - в наличии, False - выдана).
        """
        self.status = status
