import math

print("РЕШЕНИЕ ЗАДАЧ 1-15")
print("=" * 50)

# Задание 1
print("\n1. Вывести N раз число K:")
K, N = 5, 3
print(f"K = {K}, N = {N}")
result = [K] * N
print(f"Результат: {result}")

# Задание 2
print("\n2. Числа от A до B (по возрастанию):")
A, B = 3, 7
numbers = list(range(A, B + 1))
N_count = len(numbers)
print(f"A = {A}, B = {B}")
print(f"Числа: {numbers}")
print(f"Количество чисел N = {N_count}")

# Задание 3
print("\n3. Числа от A до B (по убыванию, не включая A и B):")
A, B = 3, 7
numbers = list(range(B - 1, A, -1))
N_count = len(numbers)
print(f"A = {A}, B = {B}")
print(f"Числа: {numbers}")
print(f"Количество чисел N = {N_count}")

# Задание 4
print("\n4. Таблица стоимости товара:")
price = 20.4
print(f"Цена за 1 шт: {price} руб")
print("Количество | Стоимость")
for i in range(1, 11):
    cost = price * i
    print(f"{i:9} | {cost:8.1f} руб")

# Задание 5
print("\n5. Квадраты чисел от A до B с шагом H:")
A, B, H = 1, 10, 2
print(f"A = {A}, B = {B}, H = {H}")
print("Число | Квадрат")
for i in range(A, B + 1, H):
    print(f"{i:5} | {i**2:7}")

# Задание 6
print("\n6. Положительные числа от A до B с шагом H:")
A, B, H = -3, 8, 2
print(f"A = {A}, B = {B}, H = {H}")
positive_numbers = [i for i in range(A, B + 1, H) if i > 0]
print(f"Положительные числа: {positive_numbers}")

# Задание 7
print("\n7. Сумма чисел от A до B:")
A, B = 1, 5
total_sum = sum(range(A, B + 1))
print(f"A = {A}, B = {B}")
print(f"Сумма = {total_sum}")

# Задание 8
print("\n8. Произведение чисел от A до B:")
A, B = 1, 5
product = 1
for i in range(A, B + 1):
    product *= i
print(f"A = {A}, B = {B}")
print(f"Произведение = {product}")

# Задание 9
print("\n9. Сумма квадратов чисел от A до B:")
A, B = 1, 3
sum_squares = sum(i**2 for i in range(A, B + 1))
print(f"A = {A}, B = {B}")
print(f"Сумма квадратов = {sum_squares}")

# Задание 10
print("\n10. Стоимость конфет от 1 до 2 кг с шагом 0.2:")
price_per_kg = 150.0
print(f"Цена за 1 кг: {price_per_kg} руб")
print("Вес (кг) | Стоимость")
weight = 1.0
while weight <= 2.0:
    cost = price_per_kg * weight
    print(f"{weight:7.1f} | {cost:8.1f} руб")
    weight = round(weight + 0.2, 1)

# Задание 11
print("\n11. Квадрат числа через сумму нечетных:")
N = 5
square = sum(2*i - 1 for i in range(1, N + 1))
print(f"N = {N}")
print(f"N² = {square} (проверка: {N**2})")

# Задание 12
print("\n12. Целые степени числа A от 1 до N:")
A, N = 2, 5
print(f"A = {A}, N = {N}")
print("Степень | Результат")
for i in range(1, N + 1):
    print(f"{i:7} | {A**i:9}")

# Задание 13
print("\n13. Наибольшее K, где K² ≤ N:")
N = 17
K = int(math.sqrt(N))
print(f"N = {N}")
print(f"K = {K} (K² = {K**2} ≤ {N})")

# Задание 14
print("\n14. Наибольшее K, где 3^K < N:")
N = 100
K = 0
while 3**(K + 1) < N:
    K += 1
print(f"N = {N}")
print(f"K = {K} (3^{K} = {3**K} < {N})")

# Задание 15
print("\n15. Разбиение отрезка [A,B] на N равных частей:")
N = 4
A, B = 0, 10
H = (B - A) / N
points = [A + i * H for i in range(N + 1)]
print(f"A = {A}, B = {B}, N = {N}")
print(f"Длина отрезка H = {H:.2f}")
print(f"Точки разбиения: {[round(p, 2) for p in points]}")
