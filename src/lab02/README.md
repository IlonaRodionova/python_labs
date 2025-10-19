# Лабораторная 2
## Задание 1
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
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
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten")
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![arrays.png](..%2F..%2Fimages%2Flab02%2Farrays.png)
## Задание 2

```
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
```
![matrix.png](..%2F..%2Fimages%2Flab02%2Fmatrix.png)

## Задание 3

```
def format_record(tuuple):
    if type(tuuple) != tuple:
        return 'TypeError'
    if len(tuuple) != 3:
        return 'ValueError'

    if tuuple[0] == '' or tuuple[1] == '':
        return 'ValueError'

    if type(tuuple[0]) != str or type(tuuple[1]) != str or type(tuuple[2]) != float:
        return 'TypeError'

    # Реализуем обработку фамилии
    fio = tuuple[0].split()
    m = len(fio) - 1
    fio_str = f'{fio[0][0].upper()}{fio[0][1:]} '
    for i in range(1, m + 1):
        fio_str += f'{fio[i][0].upper()}.'
    fio_str += ','

    # Реализуем обработку группы
    group_str = f' гр. {tuuple[1]},'

    # Реализуем обработку GPA
    GPA_str = f' GPA {tuuple[2]:.2f}'

    return fio_str + group_str + GPA_str

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

```
![tuples.png](..%2F..%2F..%2Ftuples.png)
