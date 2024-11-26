from models.library_models import Library
import os


def back() -> True:
    input("Что бы продолжить нажмите Enter ... ")
    return True


def clear_console():
    # ANSI escape sequence для очистки экрана
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main_menu():
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
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите дату издания: ")
            library.add_book(title,author, year)
            back()

        elif choice == '2':
            clear_console()
            book_id = input("Введите id книги которую вы хотите удалить: ")
            library.delete_book(book_id)
            back()

        elif choice == '3':
            clear_console()
            # Код для действия 2
            print("Вы выбрали действие 3")

        elif choice == '4':
            clear_console()
            library.show_all_books()
            back()

        elif choice == '5':
            clear_console()
            book_id=input("Введите id книги статус которой вы хотите изменить: ")
            status=input("Введите новый статус")
            library.change_status_book(book_id, status)

        elif choice == '6':
            clear_console()
            # Код для действия 2
            print("Вы выбрали действие 6")
        elif choice == '7':
            clear_console()
            # Код для действия 2
            print("Вы выбрали действие 7")
        elif choice == '8':
            clear_console()
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
