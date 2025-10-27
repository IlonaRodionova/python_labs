import os

# Создаем папку data если её нет
if not os.path.exists("data"):
    os.makedirs("data")

# Создаем тестовый файл
with open("data/input.txt", "w", encoding="utf-8") as f:
    f.write("Привет мир! Это тестовый текст для проверки.\n")
    f.write("Программа должна подсчитать слова в этом тексте.\n")
    f.write("Привет еще раз!\n")

print("Тестовый файл data/input.txt создан")


from src.lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir

print(" Тест 1: Чтение файла")
try:
    text = read_text("data/input.txt", encoding="utf-8")
    print(f"Успешно прочитано: {len(text)} символов")
    print(f"Текст: {text[:100]}...")
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
    print("Создай файл data/input.txt с текстом")
except UnicodeDecodeError as e:
    print(f"Ошибка кодировки: {e}")
    try:
        text = read_text("data/input.txt", encoding="cp1251")
        print(f"С кодировкой cp1251: {text[:100]}...")
    except Exception as e2:
        print(f"cp1251 тоже не работает: {e2}")

print("\n Тест 2: Создание CSV")
test_data = [
    ("word", "count"),
    ("привет", 2),
    ("мир", 1),
    ("текст", 1)
]

write_csv(test_data, "data/output.csv", header=("word", "count"))
print("CSV файл создан: data/output.csv")

print("\n Тест 3: Создание папок")
ensure_parent_dir("results/new_folder/test.csv")
print("Папки созданы")

print("\n Тест 4: Пустой CSV")
write_csv([], "data/empty.csv")
print("Пустой файл создан")

print("\nВсе тесты завершены!")