# Лабораторная 4
## Задание 1
```
from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
   p = Path(path)
   return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)

    # Проверяем, что все строки одинаковой длины
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {first_len}")

    # Записываем в файл
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)


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
