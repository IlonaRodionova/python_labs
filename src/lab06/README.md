# Лабораторная 6
## Задание 1
``` python
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
```
![1.png](..%2F..%2Fimages%2Flab06%2F1.png)

![1.1.png](..%2F..%2Fimages%2Flab06%2F1.1.png)

## Задание 2

``` python
import argparse
from hmac import digest_size

from modules_lab06 import json_to_csv, csv_to_json, csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="CLI-конвертер")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv", help="Json to Csv convert function")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Csv to Json convert function")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Csv to XLSX convert function")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
```
![2.png](..%2F..%2Fimages%2Flab06%2F2.png)
