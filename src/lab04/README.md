# Лабораторная 4
## Задание 1
```
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)

    # Проверяем что файл имеет расширение .txt
    if p.suffix.lower() not in ['.txt', '.csv']:
        raise ValueError("Функция read_text работает только с .txt и .csv файлами")
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] = None) -> None:
    p = Path(path)

    # Проверяем что файл имеет расширение .csv или .txt
    if p.suffix.lower() not in ['.csv', '.txt']:
        raise ValueError("Функция write_csv работает только с .csv и .txt файлами")

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
![1.png](..%2F..%2Fimages%2Flab04%2F1.png)
![111.png](..%2F..%2Fimages%2Flab04%2F111.png)
## Задание 2

```
from lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    txt = tokenize(normalize(read_text("data/input.txt")))
    a = [("word",len(txt))]
    for el in top_n(count_freq(txt)):
        a.append((el[0],el[1]))
    write_csv(a, "data/report.csv")

if __name__ == "__main__":
    main()

```
![2.png](..%2F..%2Fimages%2Flab04%2F2.png)
