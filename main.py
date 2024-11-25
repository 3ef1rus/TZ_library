import uuid
from time import perf_counter
from typing import List, Optional

from data import save_books_to_json, read_from_file


class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 year: int,
                 id:Optional[uuid.UUID] = None,
                 status:Optional[bool] = None
                 ) -> None:
        self.title = title
        self.author = author
        self.year = year
        if id is None:
            self.id:uuid.UUID  = uuid.uuid4().hex
        else:
            self.id = id
        if status is None:
            self.status: bool = True
        else:
            self.status = status

    def show_book(self):
        status="В наличии" if self.status is True else "Выдана"
        print(f"id книги: {self.id},"
              f" Название книги: {self.title},"
              f" Автор книги: {self.author},"
              f" Год издания: {self.year},"
              f" Состояние книги: {status}")


    def change_status(self, status:bool):
        self.status = status


class Library:

    def __init__(self)->None:
        self.books: List[Book] = []

    def load_books_from_file(self)->None:
        data = read_from_file('template_books.json')
        for book_data in data:
            book = Book(title=book_data["title"],
                        author=book_data["author"],
                        year=book_data["year"],
                        id=book_data["id"],
                        status=book_data["status"]
                        )
            self.books.append(book)

    def add_book(
            self,
            title:str,
            author:str,
            year:int
    )->None:
        self.books.append(Book(title, author, year))

    def delete_book(self, book_id:uuid.UUID)->None:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Книга удалена")
                return None
        print(f"Книги с id {book_id} не существует")

    def show_all_books(self):
        for book in self.books:
            book.show_book()


    def change_status_book(self, book_id:uuid.UUID,status:str)->None:
        data=True if status == "В наличии" else False
        for book in self.books:
            if book.id == book_id:
                book.change_status(True)
                print("Статус изменен")
                return
        print(f"Книги с id {book_id} не существует")


    def search_book(self,title=None,author=None,year=None):
        if title is not None:
            for book in self.books:
                if book.title == title:
                    book.show_book()
            print("Книги с таким название не найдена")
            return

        if author is not None:
            for book in self.books:
                if book.author == author:
                    book.show_book()
            print("Книги с автором не найдена")
            return

        if year is not None:
            for book in self.books:
                if book.year == year:
                    book.show_book()
            print("Книги такого когда выпуска не найдена")
            return


# save_books_to_json(books, 'template_books.json')
library = Library()
library.load_books_from_file()
# library.add_book("Гарри Поттер и философский камень","Дж.К. Роулинг","1997")
# library.show_all_books()
# library.delete_book("547d13d9edc24cc9b4fe0478fe59a235")
# library.delete_book("886dd68ff2ff478888a8e0235cd8f655")
library.show_all_books()
library.search_book(year=1967)
