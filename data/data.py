import json


def read_from_file(filename: str) -> list[dict]:
    """
    Считывает данные из указанного JSON-файла.

    Функция открывает указанный файл в режиме чтения,
    парсит JSON-данные и возвращает их в виде списка словарей.
    Структура данных в каждом словаре зависит от содержимого JSON-файла.

    Args:
        filename (str): Путь к JSON-файлу для чтения.

    Returns:
        list[dict]: Список словарей, представляющих данные из JSON-файла.

    Raises:
        Exception: В случае возникновения ошибок при записи в файл.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    except Exception as e:
        print(f"Произошла ошибка при работе с JSON-данных: {e}")


def save_to_json(data: list[dict], filename: str) -> None:
    """
    Сохраняет список словарей в JSON-файл.

    Функция принимает список словарей, и имя файла для сохранения.
    Сохраняет данные в формате JSON с отступом для лучшей читаемости.

    Args:
        data (list[dict]): Список словарей.
        filename (str): Имя JSON-файла для сохранения данных.

    Raises:
        Exception: В случае возникновения ошибок при записи в файл.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Произошла ошибка при работе с JSON-данных: {e}")
