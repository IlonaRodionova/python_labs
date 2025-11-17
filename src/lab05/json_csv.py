import json
import csv
from pathlib import Path

def json_to_csv(json_path, csv_path):
    # Проверяем файл
    if not Path(json_path).exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    # Читаем JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Проверяем данные
    if not data or not isinstance(data, list):
        raise ValueError("JSON должен быть непустым списком")

    # Получаем все названия колонок
    all_columns = set()
    for item in data:
        all_columns.update(item.keys())

    columns = sorted(all_columns)  # Сортируем по алфавиту

    # Создаем папку для результата
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)

    # Записываем CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for item in data:
            row = {col: item.get(col, '') for col in columns}
            writer.writerow(row)


def csv_to_json(csv_path, json_path):
    # Проверяем файл
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    # Читаем CSV
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    if not data:
        raise ValueError("CSV файл пустой")

    # Создаем папку для результата
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)

    # Записываем JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)






