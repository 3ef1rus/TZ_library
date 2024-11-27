from typing import List, Optional
from data.data import save_to_json, read_from_file
from models.book_models import Book


class Library:
    """
    Управляет коллекцией книг. Позволяет загружать, сохранять, добавлять, удалять,
    изменять статус и искать книги.

    Attributes:
        books (list[Book]): Список объектов Book, содержащих информацию о каждой книге.
    """

    def __init__(self) -> None:
        """Инициализирует пустой список книг."""
        self.books: List[Book] = []

    def load_books_from_file(self, filename: str) -> None:
        """
        Загружает книги из JSON-файла.

        Args:
            filename (str): Имя JSON-файла, содержащего данные о книгах.

        Raises:
            ValueError: Если файл не найден или данные в файле неверны.
        """

        data = read_from_file(filename=filename)

        required_fields = ["title", "author", "year", "id", "status"]

        for book_data in data:
            if not all(field in book_data for field in required_fields):
                print(f"Ошибка в данных книги: отсутствуют обязательные поля. Книга пропущена.")
                continue

            book = Book(title=book_data["title"],
                        author=book_data["author"],
                        year=book_data["year"],
                        id=book_data["id"],
                        status=book_data["status"]
                        )
            self.books.append(book)

        print("Все книги загружены")

    def save_books_to_file(self, filename: str) -> None:
        """
        Сохраняет книги в JSON-файл.

        Args:
            filename (str): Имя JSON-файла, в который будут сохранены данные о книгах.
        """
        books_data = [book.__dict__ for book in self.books]
        save_to_json(data=books_data, filename=filename)
        print("Все книги сохранены")

    def add_book(
            self,
            title: str,
            author: str,
            year: int
    ) -> None:
        """
        Добавляет новую книгу в коллекцию.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        self.books.append(Book(title, author, year))
        print("Книга добавлена")

    def delete_book(self, book_id: str) -> None:
        """
        Удаляет книгу из коллекции по ее идентификатору.

        Args:
            book_id (str): Идентификатор книги, которую нужно удалить.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Книга удалена")
        print(f"Книги с id {book_id} не существует")

    def show_all_books(self) -> None:
        """
        Отображает информацию обо всех книгах в коллекции.

        Вызывает метод show_book() для каждого объекта Book в списке self.books.
        """
        for book in self.books:
            book.show_book()

    def change_status_book(self, book_id: str, status: str) -> None:
        """
        Изменяет статус книги по ее идентификатору.

        Args:
            book_id (str): Идентификатор книги, для которой нужно изменить статус.
            status (str): Новый статус книги ("В наличии" или "Не в наличии").
        """
        data = True if status == "В наличии" else False
        for book in self.books:
            if book.id == book_id:
                book.change_status(data)
                print("Статус изменен")
        print(f"Книги с id {book_id} не существует")

    def search_book(
            self,
            title: Optional[str] = None,
            author: Optional[str] = None,
            year: Optional[int] = None
    ) -> None:
        """
        Функция для поиска книг по заданным параметрам.

        Args:
            title (str, optional): Заголовок книги. По умолчанию None.
            author (str, optional): Автор книги. По умолчанию None.
            year (int, optional): Год издания книги. По умолчанию None.
        """
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
