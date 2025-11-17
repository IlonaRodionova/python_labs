import os, sys
from itertools import count
from pathlib import Path
import argparse

from modules_lab06 import normalize, tokenize, count_freq, top_n

def cat(path, numbered=False):
    k = 1
    with open(path, encoding="utf-8") as f:
        for line in f:
            if numbered:
                print(f'{k} {line.strip()}')
            else:
                print(line.strip())
            k += 1

def stats(path, top_k=5):
    text = Path(path).read_text(encoding="utf-8")
    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top = top_n(freq, top_k)

    print(f'Всего слов: {len(tokens)}')
    print(f'Различных слов: {len(freq)}\n')
    print(f'Топ-{top_k} слов:')
    for word, cnt in top:
        print(f"{word}: {cnt}")

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", dest="flag", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", dest="top_words", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.flag)
    elif args.command == "stats":
        stats(args.input, args.top_words)

if __name__ == "__main__":
    main()