import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from lib.text import normalize, tokenize, count_freq, top_n


# Параметризованные тесты для normalize
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
        ("ТЕКСТ!! С... punctuation?", "текст!! с... punctuation?"),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


# Параметризованные тесты для tokenize
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


# Параметризованные тесты для count_freq
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


# Параметризованные тесты для top_n
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


# Дополнительные тесты как у одногруппника
def test_normalize_special_cases():
    """Тест специальных случаев нормализации"""
    assert normalize("  Много   пробелов  ") == "много пробелов"
    assert normalize("Разные\nпереводы\tстрок") == "разные переводы строк"


def test_tokenize_edge_cases():
    """Тест граничных случаев токенизации"""
    assert tokenize("word") == ["word"]
    assert tokenize("a-b-c") == ["a-b-c"]
    assert tokenize("test1 test2 test3") == ["test1", "test2", "test3"]


def test_count_freq_edge_cases():
    """Тест граничных случаев подсчета частот"""
    assert count_freq(["a", "A", "a"]) == {"a": 2, "A": 1}  # Регистр важен
    assert count_freq(["word-with-dash"]) == {"word-with-dash": 1}


def test_top_n_edge_cases():
    """Тест граничных случаев top_n"""
    # Тест когда n больше количества элементов
    assert top_n({"a": 1}, 10) == [("a", 1)]
    # Тест с одним элементом
    assert top_n({"single": 5}, 1) == [("single", 5)]


# Интеграционные тесты
def test_full_pipeline():
    """Полный пайплайн обработки текста"""
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
    """Пайплайн со сложным текстом"""
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
