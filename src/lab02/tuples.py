def format_record(tuuple):
    if type(tuuple) != tuple:
        return "TypeError"
    if len(tuuple) != 3:
        return "ValueError"

    if tuuple[0] == "" or tuuple[1] == "":
        return "ValueError"

    if type(tuuple[0]) != str or type(tuuple[1]) != str or type(tuuple[2]) != float:
        return "TypeError"

    # Реализуем обработку фамилии
    fio = tuuple[0].split()
    m = len(fio) - 1
    fio_str = f"{fio[0][0].upper()}{fio[0][1:]} "
    for i in range(1, m + 1):
        fio_str += f"{fio[i][0].upper()}."
    fio_str += ","

    # Реализуем обработку группы
    group_str = f" гр. {tuuple[1]},"

    # Реализуем обработку GPA
    GPA_str = f" GPA {tuuple[2]:.2f}"

    return fio_str + group_str + GPA_str


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
