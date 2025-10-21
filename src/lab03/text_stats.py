import sys
import os

# sys.path.append(r'C:\Users\Илона\Desktop\python_labs\src\lib')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))) # относительный путь к файлу (позволяет удобно использовать данный код на различных устройствах)
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

# echo "Hello world!!! Hello!" | python src/lab03/text_stats.py