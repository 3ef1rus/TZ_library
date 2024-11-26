from models.library_models import Library


def main_menu():
    library = Library()
    while True:
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
            title=input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите дату издания: ")
            library.add_book(title=title,author=author,year=year)

        elif choice == '2':
            # Код для действия 2
            print("Вы выбрали действие 2")
        elif choice == '3':
            # Код для действия 2
            print("Вы выбрали действие 3")
        elif choice == '4':
            # Код для действия 2
            print("Вы выбрали действие 4")
        elif choice == '5':
            # Код для действия 2
            print("Вы выбрали действие 5")
        elif choice == '6':
            # Код для действия 2
            print("Вы выбрали действие 6")
        elif choice == '7':
            # Код для действия 2
            print("Вы выбрали действие 7")
        elif choice == '8':
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")