import re

def validation_title(title) -> bool:
    if not title:
        print("Поле не может быть пустым")
        return False


def validation_author(author) -> bool:
    if not author:
        print("Поле не может быть пустым")
        return False

    pattern = r'^[а-яА-Я\s-]+$'
    return bool(re.match(pattern, author))


def validation_year(year) -> bool:
    if not year:
        print("Поле не может быть пустым")
        return False

    if not year.isdigit():
        print("Поле не может содержать символы")
        return False
