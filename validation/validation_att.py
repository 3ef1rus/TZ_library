import re


def validation_title(title: str) -> bool:
    try:
        if not title:
            raise ValueError("Поле не может быть пустым")
        return True
    except ValueError as e:
        print(e)
        return False


def validation_author(author: str) -> bool:
    try:
        if not author:
            raise ValueError("Поле не может быть пустым")

        pattern = r'^[а-яА-ЯёЁ\s-]{2,50}$'
        if bool(re.match(pattern, author)) is True:
            return True
        else:
            raise ValueError("Неправильный формат имени")
    except ValueError as e:
        print(e)
        return False


def validation_year(year: str) -> bool:
    try:
        if not year:
            raise ValueError("Поле не может быть пустым")

        if not int(year):
            raise ValueError("Поле не может содержать символы")
        return True
    except ValueError as e:
        print(e)
        return False
