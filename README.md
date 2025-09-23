# Лабораторная 1
## Задание 1

```
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age + 1}')
```

<img width="1034" height="1061" alt="01_greeting" src="https://github.com/user-attachments/assets/b3ff1fe7-c448-41a4-a4ce-a46f6490e585" />

## Задание 2

```
a = float(input())
b = float(input())
print(f'sum={a+b}; avg={(a+b)/2}')
```
<img width="973" height="677" alt="02_sum_avg" src="https://github.com/user-attachments/assets/fe8b6d2b-6f3e-4eef-949c-c3055f3f834f" />

## Задание 3

```
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f}")
print(f"НДС: {vat_amount:.2f}")
print(f"Итого к оплате {total:.2f}")
```
<img width="734" height="926" alt="03_discount_vat" src="https://github.com/user-attachments/assets/76b0ce63-e8c6-4ba5-b5ea-ff3a16039b61" />

## Задание 4

```
m = int(input())
print(f'{m//60}:{m % 60}')
```
<img width="683" height="785" alt="04_minutes_to_hhmm" src="https://github.com/user-attachments/assets/e85a1b3c-48dc-4a67-8ec3-4f6a789de4c1" />

## Задание 5

```
fio = input('ФИО: ')
ini = fio.split()
fio = fio.replace(' ', '')
i = ini[0][:1] + ini[1][:1] + ini[2][:1]
print(f'Инициалы: {i}')
print(f'Длина (символов): {len(fio)}')
```
<img width="847" height="825" alt="05_initials_and_len" src="https://github.com/user-attachments/assets/4f63cdff-61fa-4d58-bcd7-2d43eee88247" />
