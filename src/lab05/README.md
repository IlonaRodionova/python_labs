# Лабораторная 5
## Задание 1
``` python
import json
import csv
from pathlib import Path


def json_to_csv(json_path, csv_path):
    """JSON → CSV"""
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
    """CSV → JSON"""
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

```

## Задание 2

``` python
import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path, xlsx_path):
    """CSV → Excel"""
    # Проверяем файл
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    # Читаем CSV
    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV файл пустой")

    # Создаем папку для результата
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)

    # Создаем Excel файл
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Копируем данные из CSV
    for row in rows:
        ws.append(row)

    # Настраиваем ширину колонок
    for col in ws.columns:
        max_length = 8  # минимальная ширина
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        # Устанавливаем ширину
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max_length + 2

    # Сохраняем файл
    wb.save(xlsx_path)

```

