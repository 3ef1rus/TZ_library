import uuid
import typing


class Book:
    def __init__(self,title, author, year):
        self.id:uuid.UUID=uuid.uuid4()
        self.title:str = title
        self.author:str = author
        self.year:int = year
        self.status:bool = True


class Library:

    def __init__(self):
        self.books:typing.List[Book] = []

    def add_book(self,title,author,year):
        self.books.append(Book(title,author,year))

    def delete_book(self,book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)

books = [
    Book("Война и мир", "Лев Толстой", year=1869),
    Book("Преступление и наказание", "Фёдор Достоевский", year=1866),
    Book("Мастер и Маргарита", "Михаил Булгаков", year=1967),
    Book("Сто лет одиночества", "Габриэль Гарсиа Маркес", year=1967),
    Book("1984", "Джордж Оруэлл", 1949),
    Book("Божественная комедия", "Данте Алигьери", year=1321),
    Book("Гордость и предубеждение", "Джейн Остин", year=1813),
    Book("Лолита", "Владимир Набоков", year=1955),
    Book("Моби Дик", "Герман Мелвилл", year=1851),
    Book("Маленький принц", "Антуан де Сент-Экзюпери", year=1943),
]
library = Library()
for el in books:
    library.add_book(el.title,el.author,el.year)

