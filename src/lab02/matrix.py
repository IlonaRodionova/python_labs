def check_rectangular(mat):
    """
    Проверяет, является ли матрица прямоугольной (все строки одинаковой длины).

    Args:
        mat: Матрица (список списков) для проверки

    Returns:
        bool: True если матрица прямоугольная, False если рваная
    """
    if not mat:
        return True
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            return False
    return True


def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Транспонирует матрицу (меняет строки и столбцы местами).

    Args:
        mat: Прямоугольная матрица для транспонирования

    Returns:
        Транспонированная матрица

    Raises:
        ValueError: Если матрица рваная (строки разной длины)

    """
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Вычисляет суммы элементов по каждой строке матрицы.

    Args:
        mat: Прямоугольная матрица

    Returns:
        Список сумм по строкам

    Raises:
        ValueError: Если матрица рваная (строки разной длины)

    """
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Вычисляет суммы элементов по каждому столбцу матрицы.

    Args:
        mat: Прямоугольная матрица

    Returns:
        Список сумм по столбцам

    Raises:
        ValueError: Если матрица рваная (строки разной длины)

    """
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    if not mat:
        return []
    return [sum(col) for col in zip(*mat)]
