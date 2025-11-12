import random

print("ФИЛЬТРАЦИЯ И СОРТИРОВКА СПИСКОВ")
print("=" * 50)

# Общий тестовый список
lst = [12, -5, 8, 25, -3, 15, 7, 30, -8, 18, 10, 22, -12, 9, 27]
print(f"Исходный список: {lst}")

# Задание 1
print("\n1. Все нечетные числа, упорядоченные по убыванию:")
odd_desc = sorted([x for x in lst if x % 2 != 0], reverse=True)
print(f"Результат: {odd_desc}")

# Задание 2
print("\n2. Все положительные числа, упорядоченные по возрастанию:")
positive_asc = sorted([x for x in lst if x > 0])
print(f"Результат: {positive_asc}")

# Задание 3
print("\n3. Все положительные числа, упорядоченные по убыванию:")
positive_desc = sorted([x for x in lst if x > 0], reverse=True)
print(f"Результат: {positive_desc}")

# Задание 4
print("\n4. Все четные числа, упорядоченные по возрастанию:")
even_asc = sorted([x for x in lst if x % 2 == 0])
print(f"Результат: {even_asc}")

# Задание 5
print("\n5. Все числа больше k=10, упорядоченные по убыванию:")
k5 = 10
greater_k_desc = sorted([x for x in lst if x > k5], reverse=True)
print(f"k = {k5}")
print(f"Результат: {greater_k_desc}")

# Задание 6
print("\n6. Все числа больше 10, упорядоченные по возрастанию:")
greater_10_asc = sorted([x for x in lst if x > 10])
print(f"Результат: {greater_10_asc}")

# Задание 7
print("\n7. Все числа кратные 5, упорядоченные по убыванию:")
multiple_5_desc = sorted([x for x in lst if x % 5 == 0], reverse=True)
print(f"Результат: {multiple_5_desc}")

# Задание 8
print("\n8. Все числа меньше k=15, упорядоченные по возрастанию:")
k8 = 15
less_k_asc = sorted([x for x in lst if x < k8])
print(f"k = {k8}")
print(f"Результат: {less_k_asc}")

# Задание 9
print("\n9. Все числа меньше 15, упорядоченные по убыванию:")
less_15_desc = sorted([x for x in lst if x < 15], reverse=True)
print(f"Результат: {less_15_desc}")

# Задание 10
print("\n10. Все числа кратные 3, упорядоченные по возрастанию:")
multiple_3_asc = sorted([x for x in lst if x % 3 == 0])
print(f"Результат: {multiple_3_asc}")

# Задание 11
print("\n11. Все числа кратные k=4, упорядоченные по убыванию:")
k11 = 4
multiple_k_desc = sorted([x for x in lst if x % k11 == 0], reverse=True)
print(f"k = {k11}")
print(f"Результат: {multiple_k_desc}")

# Задание 12
print("\n12. Все отрицательные числа, упорядоченные по возрастанию:")
negative_asc = sorted([x for x in lst if x < 0])
print(f"Результат: {negative_asc}")

# Задание 13
print("\n13. Все числа на нечетных позициях, упорядоченные по убыванию:")
odd_positions_desc = sorted([lst[i] for i in range(len(lst)) if (i+1) % 2 != 0], reverse=True)
print(f"Нечетные позиции: {[lst[i] for i in range(len(lst)) if (i+1) % 2 != 0]}")
print(f"Результат: {odd_positions_desc}")

# Задание 14
print("\n14. Все двузначные числа, упорядоченные по возрастанию:")
two_digit_asc = sorted([x for x in lst if 10 <= abs(x) <= 99])
print(f"Результат: {two_digit_asc}")

# Задание 15
print("\n15. Все числа на четных позициях, упорядоченные по возрастанию:")
even_positions_asc = sorted([lst[i] for i in range(len(lst)) if (i+1) % 2 == 0])
print(f"Четные позиции: {[lst[i] for i in range(len(lst)) if (i+1) % 2 == 0]}")
print(f"Результат: {even_positions_asc}")
