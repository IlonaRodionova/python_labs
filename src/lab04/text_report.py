import sys
from pathlib import Path
from collections import Counter

# Добавляем путь к библиотекам
sys.path.append(str(Path(__file__).parent.parent / "lib"))
from lib.text import normalize, tokenize

from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main():
    if len(sys.argv) != 3:
        print("Использование: python text_report.py входной_файл выходной_файл")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Читаем текст
    text = read_text(input_file)

    # Считаем частоты
    freq = frequencies_from_text(text)

    # Сортируем слова
    sorted_words = sorted_word_counts(freq)

    # Записываем CSV
    write_csv(sorted_words, output_file, header=("word", "count"))

    print(f"Обработано слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Отчет сохранен в: {output_file}")


if __name__ == "__main__":
    main()