import json

def read_from_file(filename:str)->list:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    except Exception as e:
        print(f"Произошла ошибка при работе с JSON-данных: {e}")

def save_books_to_json(data:list[dict], filename:str)->None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Произошла ошибка при работе с JSON-данных: {e}")