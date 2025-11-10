from pathlib import Path
import csv
from typing import Iterable, Sequence


def _validate_file_extension(path: str | Path, allowed_extensions: set[str] = {'.txt', '.csv'}) -> None:
    file_path = Path(path)
    extension = file_path.suffix.lower()

    if extension not in allowed_extensions:
        raise ValueError(
            f"Этот файл не подходит! У него расширение {extension}, а нужно {', '.join(allowed_extensions)}")


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    _validate_file_extension(path, {'.txt'})
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    _validate_file_extension(path, {'.csv'})
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
