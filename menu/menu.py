from models.library_models import Library
from validation.validation_att import validation_year, validation_author, validation_title
import os


def retry_input(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = max_attempts
            while attempts > 0:
                result = func(*args, **kwargs)
                if func.__name__ == 'get_title':
                    if validation_title(result):
                        return result
                if func.__name__ == 'get_author':
                    if validation_author(result):
                        return result
                if func.__name__ == 'get_year':
                    if validation_year(result):
                        return result
                attempts -= 1
                print(f"Осталось {attempts} попыток.")
            return print("Попытки закончились , возврат в главное меню ...")

        return wrapper

    return decorator


def back() -> True:
    input("Что бы продолжить нажмите Enter ... ")
    return True


def clear_console() -> None:
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


@retry_input()
def get_title() -> str:
    title = input("Введите название книги: ")
    return title


@retry_input()
def get_author() -> str:
    author = input("Введите автора книги: ")
    return author


@retry_input()
def get_year() -> str:
    year = input("Введите дату издания: ")
    return year


def get_book_id() -> str:
    book_id = input("Введите id книги: ")
    return book_id


def get_status() -> str:
    status = input("Введите новый статус: ")
    return status


def get_filename() -> str:
    filename = input("Введите название файла: ")
    return filename


def get_mode_search() -> str:
    print("Выберите по какому критерию искать книгу: "
          "1.Название"
          "2.Автор"
          "3.Дата издания")
    mode = input("Введите номер критерия: ")
    return mode


def main_menu() -> None:
    library = Library()
    while True:
        clear_console()
        print("Выберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статуса книги")
        print("6. Загрузить книги из файла")
        print("7. Сохранить книги в файл")
        print("8. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            clear_console()
            title = get_title()
            author = get_author()
            year = get_year()
            library.add_book(title, author, int(year))
            back()

        elif choice == '2':
            clear_console()
            book_id = get_book_id()
            library.delete_book(book_id)
            back()

        elif choice == '3':
            clear_console()
            mode = get_mode_search()
            if mode == '1':
                title = get_title()
                library.search_book(title)
            elif mode == '2':
                author = get_author()
                library.search_book(author)
            elif mode == '3':
                book_id = get_book_id()
                library.search_book(book_id)
            back()

        elif choice == '4':
            clear_console()
            library.show_all_books()
            back()

        elif choice == '5':
            clear_console()
            book_id = get_book_id()
            status = get_status()
            library.change_status_book(book_id, status)
            back()

        elif choice == '6':
            clear_console()
            filename = get_filename()
            library.load_books_from_file(filename)
            back()

        elif choice == '7':
            clear_console()
            filename = get_filename()
            library.save_books_to_file(filename)
            back()

        elif choice == '8':
            clear_console()
            print("Выход...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
