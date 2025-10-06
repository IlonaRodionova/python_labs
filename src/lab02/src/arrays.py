def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Находит минимальное и максимальное значение в списке чисел.
    Args:
        nums: Список чисел (целых или с плавающей точкой)
    Returns:
        Кортеж (минимум, максимум)
    Raises:
        ValueError: Если список пустой
    """
    # Простая проверка: если список пустой - ошибка
    if len(nums) == 0:
        raise ValueError("Список не может быть пустым")

    # Находим самый маленький и самый большой элемент
    minimum = min(nums)
    maximum = max(nums)

    return (minimum, maximum)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список уникальных значений.

    Args:
        nums: Список чисел (целых или с плавающей точкой)

    Returns:
        Отсортированный список уникальных значений
    """
    # Если список пустой - возвращаем пустой список
    if len(nums) == 0:
        return []

    # Убираем повторяющиеся элементы и сортируем
    unique_nums = list(set(nums))
    unique_nums.sort()

    return unique_nums

def flatten(mat: list[list | tuple]) -> list:
    """
    Преобразует матрицу (список списков/кортежей) в один плоский список.
    Args:
        mat: Список, содержащий списки или кортежи
    Returns:
        "Расплющенный" список всех элементов
    Raises:
        TypeError: Если встречен элемент, который не список и не кортеж
    """
    result = []

    # Проверяем каждый элемент во внешнем списке
    for element in mat:
        # Если элемент - список или кортеж, добавляем все его элементы
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            # Если встретили что-то другое - ошибка
            raise TypeError(f"Элемент '{element}' не является списком или кортежем")

    return result


# Тестирование функций
if __name__ == "__main__":
    print("Тестирование min_max:")

    # Тест 1: обычный случай
    test1 = [3, -1, 5, 5, 0]
    print(f"min_max({test1}) = {min_max(test1)}")

    # Тест 2: один элемент
    test2 = [42]
    print(f"min_max({test2}) = {min_max(test2)}")

    # Тест 3: отрицательные числа
    test3 = [-5, -2, -9]
    print(f"min_max({test3}) = {min_max(test3)}")

    # Тест 4: смешанные типы
    test4 = [1.5, 2, 2.0, -3.1]
    print(f"min_max({test4}) = {min_max(test4)}")

    # Тест 5: пустой список (должна быть ошибка)
    try:
        min_max([])
    except ValueError as e:
        print(f"min_max([]) → ValueError: {e}")

    print("\nТестирование unique_sorted:")

    # Тест 1: обычный случай
    test1 = [3, 1, 2, 1, 3]
    print(f"unique_sorted({test1}) = {unique_sorted(test1)}")

    # Тест 2: пустой список
    test2 = []
    print(f"unique_sorted({test2}) = {unique_sorted(test2)}")

    # Тест 3: отрицательные числа
    test3 = [-1, -1, 0, 2, 2]
    print(f"unique_sorted({test3}) = {unique_sorted(test3)}")
    # Тест 4: смешанные типы
    test4 = [1.0, 1, 2.5, 2.5, 0]
    print(f"unique_sorted({test4}) = {unique_sorted(test4)}")

    print("\nТестирование flatten:")

    # Тест 1: список списков
    test1 = [[1, 2], [3, 4]]
    print(f"flatten({test1}) = {flatten(test1)}")

    # Тест 2: смесь списков и кортежей
    test2 = ([1, 2], (3, 4, 5))
    print(f"flatten({test2}) = {flatten(test2)}")

    # Тест 3: с пустыми списками
    test3 = [[1], [], [2, 3]]
    print(f"flatten({test3}) = {flatten(test3)}")

    # Тест 4: строка вместо списка (должна быть ошибка)
    try:
        test4 = [[1, 2], "ab"]
        flatten(test4)
    except TypeError as e:
        print(f"flatten({test4}) → TypeError: {e}")