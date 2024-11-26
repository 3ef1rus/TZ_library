import json

def read_from_file(filename:str)->list:
    with open(filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def save_books_to_json(data:list[dict], filename:str)->None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)