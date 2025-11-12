import random

print("ОПЕРАЦИИ СО СПИСКАМИ")
print("=" * 50)

# Общий тестовый список
lst = [3, 7, 2, 8, 5, 1, 9, 4, 6]
print(f"Исходный список: {lst}")

# Задание 1
print("\n1. Среднее арифметическое элементов с номерами от K до L:")
K, L = 2, 6  # Нумерация с 1 (индексы 1-5 в Python)
selected = lst[K-1:L]
average1 = sum(selected) / len(selected)
print(f"K={K}, L={L}")
print(f"Элементы: {selected}")
print(f"Среднее арифметическое: {average1:.2f}")

# Задание 2
print("\n2. Сумма всех элементов, кроме элементов от K до L:")
K, L = 3, 7
sum2 = sum(lst[:K-1]) + sum(lst[L:])
print(f"K={K}, L={L}")
print(f"Сумма: {sum2}")

# Задание 3
print("\n3. Среднее арифметическое всех элементов, кроме элементов от K до L:")
K, L = 3, 7
remaining = lst[:K-1] + lst[L:]
average3 = sum(remaining) / len(remaining) if remaining else 0
print(f"K={K}, L={L}")
print(f"Элементы: {remaining}")
print(f"Среднее арифметическое: {average3:.2f}")

# Задание 4
print("\n4. Четные числа по возрастанию индексов, затем нечетные по убыванию:")
even_forward = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0]
odd_backward = [lst[i] for i in range(len(lst)-1, -1, -1) if lst[i] % 2 != 0]
print(f"Четные: {even_forward}")
print(f"Нечетные в обратном порядке: {odd_backward}")

# Задание 5
print("\n5. Элементы с четными номерами, затем с нечетными:")
even_indices = [lst[i] for i in range(len(lst)) if (i+1) % 2 == 0]
odd_indices = [lst[i] for i in range(len(lst)) if (i+1) % 2 != 0]
print(f"Элементы с четными номерами: {even_indices}")
print(f"Элементы с нечетными номерами: {odd_indices}")

# Задание 6
print("\n6. Произведение элементов справа от максимального:")
max_index = lst.index(max(lst))
product6 = 1
for i in range(max_index + 1, len(lst)):
    product6 *= lst[i]
print(f"Максимальный элемент: {lst[max_index]} (индекс {max_index})")
print(f"Произведение элементов справа: {product6}")

# Задание 7
print("\n7. Сумма между минимальным и максимальным элементами (включая их):")
min_index = lst.index(min(lst))
max_index = lst.index(max(lst))
start, end = min(min_index, max_index), max(min_index, max_index)
sum7 = sum(lst[start:end+1])
print(f"Минимальный: {lst[min_index]}, максимальный: {lst[max_index]}")
print(f"Элементы между ними: {lst[start:end+1]}")
print(f"Сумма: {sum7}")

# Задание 8
print("\n8. Обнулить элементы между минимальным и максимальным:")
lst8 = lst.copy()
min_index = lst8.index(min(lst8))
max_index = lst8.index(max(lst8))
start, end = min(min_index, max_index), max(min_index, max_index)
for i in range(start + 1, end):
    lst8[i] = 0
print(f"Исходный список: {lst}")
print(f"После обнуления: {lst8}")

# Задание 9
print("\n9. Увеличить четные числа на заданное значение:")
increase = 10
lst9 = lst.copy()
for i in range(len(lst9)):
    if lst9[i] % 2 == 0:
        lst9[i] += increase
print(f"Увеличиваем четные на {increase}")
print(f"Исходный: {lst}")
print(f"Результат: {lst9}")

# Задание 10
print("\n10. Обнулить все нечетные числа:")
lst10 = lst.copy()
for i in range(len(lst10)):
    if lst10[i] % 2 != 0:
        lst10[i] = 0
print(f"Исходный: {lst}")
print(f"После обнуления нечетных: {lst10}")

# Задание 11
print("\n11. Минимальный элемент среди элементов с четными номерами:")
even_indices_elements = [lst[i] for i in range(1, len(lst), 2)]
min_even = min(even_indices_elements) if even_indices_elements else None
print(f"Элементы с четными номерами: {even_indices_elements}")
print(f"Минимальный: {min_even}")

# Задание 12
print("\n12. Элементы, которые больше своего правого соседа:")
greater_than_right = []
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        greater_than_right.append(i + 1)  # Нумерация с 1
print(f"Номера элементов: {greater_than_right}")
print(f"Количество таких элементов: {len(greater_than_right)}")

# Задание 13
print("\n13. Два соседних элемента с максимальной суммой:")
max_sum = 0
max_pair = (0, 0)
for i in range(len(lst) - 1):
    current_sum = lst[i] + lst[i + 1]
    if current_sum > max_sum:
        max_sum = current_sum
        max_pair = (lst[i], lst[i + 1])
print(f"Элементы: {max_pair[0]} и {max_pair[1]}")
print(f"Их сумма: {max_sum}")

# Задание 14
print("\n14. Поменять местами минимальный и максимальный элементы:")
lst14 = lst.copy()
min_index = lst14.index(min(lst14))
max_index = lst14.index(max(lst14))
lst14[min_index], lst14[max_index] = lst14[max_index], lst14[min_index]
print(f"Исходный: {lst}")
print(f"После замены: {lst14}")

# Задание 15
print("\n15. Сформировать список по правилу: каждый следующий = сумма предыдущих:")
N, A, B = 6, 2, 3
result15 = [A, B]
for i in range(2, N):
    result15.append(sum(result15))
print(f"N={N}, A={A}, B={B}")
print(f"Результат: {result15}")
