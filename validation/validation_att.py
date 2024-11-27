import re


def validation_title(title: str) -> bool:
    """
    Проверяет корректность введенного названия книги.

    Args:
        title (str): Название книги.

    Returns:
        bool: True, если название корректное, иначе False.

    Raises:
        ValueError: Если название книги пустое.
    """
    try:
        if not title:
            raise ValueError("Поле не может быть пустым")
        return True
    except ValueError as e:
        print(e)
        return False


def validation_author(author: str) -> bool:
    """
    Проверяет корректность введенного имени автора.

    Args:
        author (str): Имя автора.

    Returns:
        bool: True, если имя автора корректное, иначе False.

    Raises:
        ValueError:
            * Если имя автора пустое.
            * Если имя автора содержит недопустимые символы.
    """
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
    """
    Проверяет корректность введенного года издания.

    Args:
        year (str): Год издания.

    Returns:
        bool: True, если год издания корректный, иначе False.

    Raises:
        ValueError:
            * Если год издания пустой.
            * Если год издания содержит нечисловые символы.
    """
    try:
        if not year:
            raise ValueError("Поле не может быть пустым")

        if not int(year):
            raise ValueError("Поле не может содержать символы")
        return True
    except ValueError as e:
        print(e)
        return False
