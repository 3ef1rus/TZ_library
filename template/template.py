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

# save_books_to_json(books, 'template_books.json')
library = Library()
library.load_books_from_file()
# library.add_book("Гарри Поттер и философский камень","Дж.К. Роулинг","1997")
# library.show_all_books()
# library.delete_book("547d13d9edc24cc9b4fe0478fe59a235")
# library.delete_book("886dd68ff2ff478888a8e0235cd8f655")
# library.show_all_books()
# print("//")
# library.search_book(year=1967)
# library.search_book(title="Мастер и Маргарита")
# library.search_book(author="Михаил Булгаков")
library.change_status_book("3d81c71221a64bdea25a816a39826a7c", "выдана")
library.search_book(title="Сто лет одиночества")
