def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Находит минимальное и максимальное значение в списке чисел.

    Args:
        nums: Список чисел (целых или с плавающей точкой)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError: Если список пуст

    """
    if not nums:
        raise ValueError("Список пуст")
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список уникальных значений.

    Args:
        nums: Список чисел (целых или с плавающей точкой)

    Returns:
        Отсортированный по возрастанию список без повторяющихся значений

    """
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """
    "Расплющивает" список списков/кортежей в один список.

    Args:
        mat: Список, содержащий списки или кортежи

    Returns:
        Единый список всех элементов исходной структуры

    Raises:
        TypeError: Если встречен элемент, который не является списком или кортежем

    """
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Элемент не является списком или кортежем")
        result.extend(row)
    return result

print("min_max:")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))
