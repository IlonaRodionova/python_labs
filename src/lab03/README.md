# Лабораторная 3
## Задание 1
```
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text
print("normalize:")
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

print("tokenize:")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))


def count_freq(tokens: list[str]) -> dict[str, int]:
    c = {}
    for w in tokens:
        cu = c.get(w, 0)
        c[w] = cu + 1
    return c
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    t = []
    for w, count in freq.items():
        t.append((-count, w))
    t.sort()
    result = []
    for neg_count, w in t:
        result.append((w, -neg_count))
    return result[:n]
tok = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tok)
print("count_freq + top_n:")
print(top_n(freq, n=2))
tok_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_2 = count_freq(tok_2)
print(top_n(freq_2, n=2))
```
![text.png](..%2F..%2Fimages%2Flab03%2Ftext.png)
## Задание 2

```
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

from text import normalize, tokenize, count_freq, top_n

def main():
    a = sys.stdin.read()
    total_words = tokenize(normalize(a))
    unique_words = set(total_words)
    top_words = top_n(count_freq(total_words))
    print(f"Всего слов: {len(total_words)}")
    print(f"Уникальных слов: {len(unique_words)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# echo "Hello world!!! Hello!" | py src/lab03/text_stats.py
```
![text_stats.png](..%2F..%2Fimages%2Flab03%2Ftext_stats.png)

