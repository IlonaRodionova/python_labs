import pytest
import json
import csv
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from lab05.json_csv import json_to_csv, csv_to_json


# Базовые тесты для успешных сценариев
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
    """Параметризованный тест успешных преобразований JSON в CSV"""
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
    """Параметризованный тест успешных преобразований CSV в JSON"""
    src = tmp_path / f"{test_name}.csv"
    dst = tmp_path / f"{test_name}.json"

    src.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == expected_count


# Тесты для ошибок JSON
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
    """Параметризованный тест ошибок JSON в CSV"""
    src = tmp_path / f"{test_name}.json"
    dst = tmp_path / "output.csv"

    if file_content is None:
        with pytest.raises(expected_error):
            json_to_csv("nonexistent.json", str(dst))
    else:
        src.write_text(file_content, encoding="utf-8")
        with pytest.raises(expected_error):
            json_to_csv(str(src), str(dst))


# Тесты для ошибок CSV
@pytest.mark.parametrize(
    "test_name, file_content, expected_error",
    [
        ("file_not_found", None, FileNotFoundError),
        ("empty_file", "", ValueError),
    ],
)
def test_csv_to_json_errors(tmp_path, test_name, file_content, expected_error):
    """Параметризованный тест ошибок CSV в JSON"""
    src = tmp_path / f"{test_name}.csv"
    dst = tmp_path / "output.json"

    if file_content is None:
        with pytest.raises(expected_error):
            csv_to_json("nonexistent.csv", str(dst))
    else:
        src.write_text(file_content, encoding="utf-8")
        with pytest.raises(expected_error):
            csv_to_json(str(src), str(dst))


# Специальные тесты
def test_json_csv_roundtrip(tmp_path):
    """Тест полного цикла преобразования"""
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
    assert final_data[0]["age"] == "25"  # В CSV→JSON все становится строками


def test_csv_empty_data_with_header(tmp_path):
    """Тест для CSV только с заголовком"""
    src = tmp_path / "only_header.csv"
    dst = tmp_path / "test.json"

    src.write_text("name,age", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV файл пустой"):
        csv_to_json(str(src), str(dst))


def test_json_to_csv_creates_directories(tmp_path):
    """Тест что создаются родительские директории"""
    src = tmp_path / "test.json"
    dst = tmp_path / "deep" / "nested" / "output.csv"

    test_data = [{"name": "Test"}]
    src.write_text(json.dumps(test_data), encoding="utf-8")

    json_to_csv(str(src), str(dst))
    assert dst.exists()


def test_csv_to_json_creates_directories(tmp_path):
    """Тест что создаются родительские директории"""
    src = tmp_path / "test.csv"
    dst = tmp_path / "very" / "deep" / "output.json"

    src.write_text("name,age\nAlice,25", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    assert dst.exists()
