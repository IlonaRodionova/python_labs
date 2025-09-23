fio = input('ФИО: ')
ini = fio.split()
i = ini[0][:1] + ini[1][:1] + ini[2][:1]
print(f'Инициалы: {i}')
print(f'Длина (символов): {len(fio)}')
