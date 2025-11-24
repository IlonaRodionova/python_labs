# Лабораторная 7
## Задание 1
``` python
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
        ("\n\t\r", ""),
        ("ТЕКСТ!! С... помогите?", "текст!! с... помогите?"),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("", []),
        ("   ", []),
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (
            ["apple", "banana", "apple", "cherry"],
            {"apple": 2, "banana": 1, "cherry": 1},
        ),
        ([], {}),
        (["hello"], {"hello": 1}),
        (["a", "a", "a", "b", "b"], {"a": 3, "b": 2}),
        (["test"], {"test": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"apple": 5, "banana": 3, "cherry": 7}, 2, [("cherry", 7), ("apple", 5)]),
        (
            {"apple": 3, "banana": 3, "cherry": 1},
            3,
            [("apple", 3), ("banana", 3), ("cherry", 1)],
        ),
        ({"apple": 2}, 5, [("apple", 2)]),
        ({}, 3, []),
        ({"a": 1, "b": 2, "c": 3}, 0, []),
        ({"x": 1, "y": 1, "z": 1}, 2, [("x", 1), ("y", 1)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected


def test_normalize_special_cases():
    assert normalize("  Много       пробелов  ") == "много пробелов"
    assert normalize("Разные\nпереводы\tстрок") == "разные переводы строк"


def test_tokenize_edge_cases():
    assert tokenize("word") == ["word"]
    assert tokenize("a-b-c") == ["a-b-c"]
    assert tokenize("test1 test2 test3") == ["test1", "test2", "test3"]


def test_count_freq_edge_cases():
    assert count_freq(["a", "A", "a"]) == {"a": 2, "A": 1}  
    assert count_freq(["word-with-dash"]) == {"word-with-dash": 1}


def test_top_n_edge_cases():
    # Тест когда n больше количества элементов
    assert top_n({"a": 1}, 10) == [("a", 1)]
    # Тест с одним элементом
    assert top_n({"single": 5}, 1) == [("single", 5)]


def test_full_pipeline():
    text = "Привет мир! Привет всем. Мир прекрасен."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "привет мир! привет всем. мир прекрасен."
    assert tokens == ["привет", "мир", "привет", "всем", "мир", "прекрасен"]
    assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
    assert top_words == [("мир", 2), ("привет", 2)]


def test_full_pipeline_complex():
    text = "По-настоящему КРУТО!!! 2025 год... версия 2.0"

    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 3)

    assert "по-настоящему" in tokens
    assert "круто" in tokens
    assert "2025" in tokens
    assert "год" in tokens
    assert len(top_words) <= 3

```
![text.png](..%2F..%2Fimages%2Flab07%2Ftext.png)

## Задание 2

``` python
import pytest
import json
import csv
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from lab05.json_csv import json_to_csv, csv_to_json


@pytest.mark.parametrize(
    "test_name, data, expected_count",
    [
        ("basic", [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}], 2),
        (
            "complex_data",
            [{"name": "Alice", "age": 25, "active": True, "score": 95.5}],
            1,
        ),
        (
            "different_order",
            [{"name": "Alice", "age": 25}, {"age": 30, "name": "Bob"}],
            2,
        ),
        ("empty_values", [{"name": "Alice", "age": 25, "comment": ""}], 1),
        ("unicode", [{"name": "Алиса", "message": "Привет! 🌍"}], 1),
        (
            "different_keys",
            [{"name": "Alice", "age": 25}, {"name": "Bob", "city": "SPb"}],
            2,
        ),
    ],
)
def test_json_to_csv_success(tmp_path, test_name, data, expected_count):
    src = tmp_path / f"{test_name}.json"
    dst = tmp_path / f"{test_name}.csv"

    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == expected_count
    assert rows[0]["name"] == data[0]["name"]


@pytest.mark.parametrize(
    "test_name, csv_content, expected_count",
    [
        ("basic", "name,age\nAlice,25\nBob,30", 2),
        ("numbers", "name,age,score\nAlice,25,95.5\nBob,30,88.0", 2),
        ("special_chars", 'name,description\n"Alice","Test, comma"', 1),
    ],
)
def test_csv_to_json_success(tmp_path, test_name, csv_content, expected_count):
    src = tmp_path / f"{test_name}.csv"
    dst = tmp_path / f"{test_name}.json"

    src.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == expected_count


@pytest.mark.parametrize(
    "test_name, file_content, expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        ("invalid_json", "{ invalid json }", ValueError),
        ("empty_file", "", ValueError),
        ("not_list", '{"name": "test"}', ValueError),
        ("empty_list", "[]", ValueError),
    ],
)
def test_json_to_csv_errors(tmp_path, test_name, file_content, expected_error):
    src = tmp_path / f"{test_name}.json"
    dst = tmp_path / "output.csv"

    if file_content is None:
        with pytest.raises(expected_error):
            json_to_csv("nonexistent.json", str(dst))
    else:
        src.write_text(file_content, encoding="utf-8")
        with pytest.raises(expected_error):
            json_to_csv(str(src), str(dst))


@pytest.mark.parametrize(
    "test_name, file_content, expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        ("empty_file", "", ValueError),
    ],
)
def test_csv_to_json_errors(tmp_path, test_name, file_content, expected_error):
    src = tmp_path / f"{test_name}.csv"
    dst = tmp_path / "output.json"

    if file_content is None:
        with pytest.raises(expected_error):
            csv_to_json("nonexistent.csv", str(dst))
    else:
        src.write_text(file_content, encoding="utf-8")
        with pytest.raises(expected_error):
            csv_to_json(str(src), str(dst))


def test_json_csv_roundtrip(tmp_path):
    original_json = tmp_path / "original.json"
    intermediate_csv = tmp_path / "intermediate.csv"
    final_json = tmp_path / "final.json"

    original_data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    original_json.write_text(json.dumps(original_data), encoding="utf-8")

    json_to_csv(str(original_json), str(intermediate_csv))
    csv_to_json(str(intermediate_csv), str(final_json))

    with final_json.open(encoding="utf-8") as f:
        final_data = json.load(f)

    assert len(final_data) == 2
    assert final_data[0]["name"] == "Alice"
    assert final_data[0]["age"] == "25"


def test_csv_empty_data_with_header(tmp_path):
    src = tmp_path / "only_header.csv"
    dst = tmp_path / "test.json"

    src.write_text("name,age", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV файл пустой"):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_creates_directories(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "deep" / "nested" / "output.csv"

    test_data = [{"name": "Test"}]
    src.write_text(json.dumps(test_data), encoding="utf-8")

    json_to_csv(str(src), str(dst))
    assert dst.exists()


def test_csv_to_json_creates_directories(tmp_path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "very" / "deep" / "output.json"

    src.write_text("name,age\nAlice,25", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    assert dst.exists()

```
![json_csv.png](..%2F..%2Fimages%2Flab07%2Fjson_csv.png)

## Задание 3
### До:
![black_before.png](..%2F..%2Fimages%2Flab07%2Fblack_before.png)
### После:
![black_after.png](..%2F..%2Fimages%2Flab07%2Fblack_after.png)

## Покрытие кода
![dop.png](..%2F..%2Fimages%2Flab07%2Fdop.png)