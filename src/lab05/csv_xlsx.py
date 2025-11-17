import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path, xlsx_path):
    # Проверяем файл
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    if Path(csv_path).suffix != '.csv': raise ValueError(f'Неверное расширение csv файла {Path(csv_path).suffix}')
    if Path(xlsx_path).suffix != '.xlsx': raise ValueError(f'Неверное расширение xlsx файла {Path(xlsx_path).suffix}')

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