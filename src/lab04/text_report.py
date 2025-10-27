import re
import csv
import argparse
import sys
from pathlib import Path
from collections import Counter


def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру"""
    return text.lower()


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова"""
    words = re.findall(r'\b[а-яёa-z]+\b', text, flags=re.IGNORECASE)
    return words


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Возвращает топ-N слов по частоте"""
    sorted_words = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return sorted_words[:n]


def main():
    parser = argparse.ArgumentParser(description='Анализ частоты слов в тексте')
    parser.add_argument('--in', dest='input_file', default='data/input.txt',
                        help='Входной файл (по умолчанию: data/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/report.csv',
                        help='Выходной файл (по умолчанию: data/report.csv)')
    parser.add_argument('--encoding', default='utf-8',
                        help='Кодировка файла (по умолчанию: utf-8)')

    args = parser.parse_args()

    try:
        # Чтение файла
        text = Path(args.input_file).read_text(encoding=args.encoding)

        # Создание папки для output
        Path(args.output_file).parent.mkdir(parents=True, exist_ok=True)

        # Обработка пустого файла
        if not text.strip():
            with open(args.output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['word', 'count'])
            print("Файл пустой. Создан report.csv с заголовком")
            return

        # Анализ текста
        tokens = tokenize(normalize(text))
        freq = Counter(tokens)
        sorted_words = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

        # Запись CSV
        with open(args.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['word', 'count'])
            for word, count in sorted_words:
                writer.writerow([word, count])

        # Вывод резюме
        total_words = len(tokens)
        unique_words = len(freq)
        top_5_words = top_n(freq, 5)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5_words:
            print(f"  {word} - {count}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input_file}' не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: Не удалось прочитать файл в кодировке '{args.encoding}'")
        print("Попробуйте указать другую кодировку: --encoding cp1251")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()