# Лабораторная 4
## Задание 1
``` python
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)

    # Проверяем что файл имеет расширение .txt
    if p.suffix.lower() not in ['.txt', '.csv']:
        raise ValueError("Функция read_text работает только с .txt и .csv файлами")
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] = ("word", "count")) -> None:
    p = Path(path)

    rows = list(rows)

    # Проверка одинаковой длины строк
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {first_len}")

    # Создание родительских директорий
    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


```
![io_txt_csv.jpg](..%2F..%2Fimages%2Flab04%2Fio_txt_csv.jpg)

## Задание 2

``` python
import sys
from pathlib import Path
from collections import Counter

# Добавляем путь к библиотекам
sys.path.append(str(Path(__file__).parent.parent / "lib"))

# Пробуем разные варианты импорта
try:
    from lib.text import normalize, tokenize
except ImportError:
    try:
        from text import normalize, tokenize  # пробуем без lib.
    except ImportError:
        print("Ошибка: не найден модуль text.py")
        print("Убедитесь что файл src/lib/text.py существует")
        sys.exit(1)

from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main():
    # АБСОЛЮТНЫЕ пути - всегда будут вести в папку data
    project_root = Path(__file__).parent.parent.parent
    input_file = project_root / "data" / "lab04" / "input.txt"
    output_file = project_root / "data" / "lab04" / "report.csv"

    try:
        # Читаем текст
        text = read_text(input_file)

        # Считаем частоты
        freq = frequencies_from_text(text)

        # Сортируем слова
        sorted_words = sorted_word_counts(freq)

        # Записываем CSV
        write_csv(sorted_words, output_file, header=("word", "count"))

        # Топ-5 слов
        top_5 = sorted_words[:5]

        print(f"Всего слов: {sum(freq.values())}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"  {word}: {count}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        print("Создайте файл data/lab04/input.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
![text_report.jpg](..%2F..%2Fimages%2Flab04%2Ftext_report.jpg)
