import json

def read_from_file(filename:str)->list:
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def save_books_to_json(books, filename):
  """Сохраняет список книг в JSON-файл.

  Args:
    books: Список объектов класса Book.
    filename: Имя файла для сохранения.
  """

  # Преобразуем каждый объект Book в словарь
  books_data = [book.__dict__ for book in books]

  # Сохраняем данные в JSON-файл с отступами для лучшей читаемости
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump(books_data, f, indent=4, ensure_ascii=False)