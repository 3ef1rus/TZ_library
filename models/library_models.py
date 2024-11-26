import uuid
from typing import List, Optional, Union
from data.data import save_books_to_json, read_from_file
from models.book_models import Book


class Library:

    def __init__(self) -> None:
        self.books: List[Book] = []

    def load_books_from_file(self, filename) -> None:
        data = read_from_file(filename=filename)
        for book_data in data:
            book = Book(title=book_data["title"],
                        author=book_data["author"],
                        year=book_data["year"],
                        id=book_data["id"],
                        status=book_data["status"]
                        )
            self.books.append(book)

    def save_books_to_file(self, filename) -> None:
        books_data = [book.__dict__ for book in self.books]
        save_books_to_json(data=books_data, filename=filename)

    def add_book(
            self,
            title: str,
            author: str,
            year: int
    ) -> str:
        self.books.append(Book(title, author, year))
        print("Книга добавлена")

    def delete_book(self, book_id: str) -> str:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Книга удалена")
                return
        print(f"Книги с id {book_id} не существует")

    def show_all_books(self):
        for book in self.books:
            book.show_book()

    def change_status_book(self, book_id: uuid.UUID, status: str) -> str:
        data = True if status == "В наличии" else False
        for book in self.books:
            if book.id == book_id:
                book.change_status(data)
                print("Статус изменен")
                return
        print(f"Книги с id {book_id} не существует")

    def search_book(self, title=None, author=None, year=None) -> str:
        count = 0
        if title is not None:
            for book in self.books:
                if book.title == title:
                    book.show_book()
                    count += 1

        if author is not None:
            for book in self.books:
                if book.author == author:
                    book.show_book()
                    count += 1

        if year is not None:
            for book in self.books:
                if book.year == year:
                    book.show_book()
                    count += 1

        if count > 0:
            return
        else:
            print("Книги с такими параметрами не найдена")
