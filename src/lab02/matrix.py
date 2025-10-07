def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    def check_rectangular(mat):
        if not mat:
            return True
        length = len(mat[0])
        for row in mat:
            if len(row) != length:
                return False
        return True
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    def check_rectangular(mat):
        if not mat:
            return True
        length = len(mat[0])
        for row in mat:
            if len(row) != length:
                return False
        return True
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    if not mat:
        return []
    return [sum(col) for col in zip(*mat)]
print("transpose")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

print("row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))