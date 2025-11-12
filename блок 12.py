import random
from collections import Counter

print("ОПЕРАЦИИ С КОРТЕЖАМИ")
print("=" * 50)

# Задание 1
print("\n1. Операции с кортежами:")
# a) Кортеж из строк пользователя
user_strings = ("ПРИВЕТ", "МИР", "PYTHON", "ПРОГРАММИРОВАНИЕ")
print(f"a) Кортеж строк: {user_strings}")

# b) Словарь: строка -> длина (только заглавные буквы)
def count_uppercase_chars(s):
    return sum(1 for char in s if char.isupper())

string_dict = {s: count_uppercase_chars(s) for s in user_strings}
print(f"б) Словарь длин заглавных букв: {string_dict}")

# Задание 2
print("\n2. Операции с кортежами:")
# a) Кортеж с разными типами данных
mixed_tuple = ("строка", 42, [1, 2, 3], 3.14, {"ключ": "значение"}, True)
print(f"a) Кортеж с разными типами: {mixed_tuple}")

# b) Распаковка и сортировка по типам
tuple_list = [("текст", 1), (100, "строка"), ([1, 2], 3.14), (False, 5)]
strings = []
numbers = []
lists = []
booleans = []

for tup in tuple_list:
    for item in tup:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
        elif isinstance(item, list):
            lists.append(item)
        elif isinstance(item, bool):
            booleans.append(item)

print(f"б) Строки: {strings}")
print(f"   Числа: {numbers}")
print(f"   Списки: {lists}")
print(f"   Булевы: {booleans}")

# Задание 3
print("\n3. Операции с кортежами:")
# a) Кортеж чисел и первый элемент
numbers_tuple = (15, 8, 23, 42, 7, 56, 9, 31)
print(f"a) Кортеж чисел: {numbers_tuple}")
print(f"   Первый элемент: {numbers_tuple[0]}")

# b) Перевернутый кортеж без чисел кратных 3
reversed_filtered = tuple(x for x in reversed(numbers_tuple) if x % 3 != 0)
print(f"б) Перевернутый без кратных 3: {reversed_filtered}")

# Задание 4
print("\n4. Операции с кортежами:")
# a) Распаковка кортежа
person_tuple = ("Иван", 25, "инженер", "Москва")
name, age, profession, city = person_tuple
print(f"a) Распаковка: Имя={name}, Возраст={age}, Профессия={profession}, Город={city}")

# b) Преобразование списка кортежей в словарь
tuple_pairs = [("яблоко", 50), ("банан", 30), ("апельсин", 70)]
result_dict = dict(sorted(tuple_pairs, key=lambda x: x[1]))
print(f"б) Отсортированный словарь: {result_dict}")

# Задание 5
print("\n5. Операции с кортежами:")
# a) Добавление элемента в кортеж
original_tuple = (1, 2, 3, 4)
new_element = 5
extended_tuple = original_tuple + (new_element,)
print(f"a) Исходный кортеж: {original_tuple}")
print(f"   После добавления {new_element}: {extended_tuple}")

# b) Форматированный кортеж с обратными строками
string_tuple = ("привет", "мир", "python")
reversed_strings = tuple(s[::-1] for s in string_tuple)
print(f"б) Строки в обратном порядке: {reversed_strings}")

# Задание 6
print("\n6. Операции с кортежами:")
# a) Преобразование кортежа в строку с разделителем
data_tuple = ("apple", "banana", "cherry")
separator = "-"
result_string = separator.join(data_tuple)
print(f"a) Кортеж: {data_tuple}")
print(f"   Строка с разделителем '{separator}': '{result_string}'")

# b) Замена последнего элемента в кортежах
tuple_list = [(1, 2, 3), ("a", "b", 5), (10, 20, "text"), (7, 8, 9)]
replacement = 99
modified_list = []
for tup in tuple_list:
    if isinstance(tup[-1], (int, float)):
        modified_list.append(tup[:-1] + (replacement,))
    else:
        modified_list.append(tup)
print(f"б) Исходный список кортежей: {tuple_list}")
print(f"   После замены на {replacement}: {modified_list}")

# Задание 7
print("\n7. Операции с кортежами:")
# a) Четвертый элемент с начала и с конца
sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
if len(sample_tuple) >= 4:
    fourth_from_start = sample_tuple[3]
    fourth_from_end = sample_tuple[-4]
    print(f"a) Кортеж: {sample_tuple}")
    print(f"   4-й элемент с начала: {fourth_from_start}")
    print(f"   4-й элемент с конца: {fourth_from_end}")

# b) Удаление пустых кортежей
tuple_list_with_empty = [(1, 2), (), (3, 4), (), (5, 6)]
cleaned_list = [tup if tup else tuple(random.randint(1, 100) for _ in range(2)) for tup in tuple_list_with_empty]
print(f"б) Исходный список: {tuple_list_with_empty}")
print(f"   После замены пустых: {cleaned_list}")

# Задание 8
print("\n8. Операции с кортежами:")
# a) Кортеж словарей
dict_tuple = (
    {"name": "Иван", "age": 25, "score": 85.5},
    {"name": "Мария", "age": 30, "score": 92.3},
    {"name": "Петр", "age": 28, "score": 78.9}
)
print(f"a) Кортеж словарей: {dict_tuple}")

# b) Сортировка по числу с плавающей точкой
sorted_tuple = tuple(sorted(dict_tuple, key=lambda x: x.get("score", 0), reverse=True))
print(f"б) Отсортированный по score (обратный порядок): {sorted_tuple}")

# Задание 9
print("\n9. Операции с кортежами:")
# a) Поиск повторяющихся элементов
test_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 3)
counter = Counter(test_tuple)
duplicates = [item for item, count in counter.items() if count > 1]
print(f"a) Кортеж: {test_tuple}")
print(f"   Повторяющиеся элементы: {duplicates}")

# b) Подсчет элементов до кортежа
mixed_list = [1, 2, 3, "текст", 4.5, (7, 8), 9, 10]
count_before_tuple = 0
sum_before_tuple = 0

for item in mixed_list:
    if isinstance(item, tuple):
        break
    if isinstance(item, (int, float)):
        count_before_tuple += 1
        sum_before_tuple += item

print(f"б) Список: {mixed_list}")
print(f"   Количество чисел до кортежа: {count_before_tuple}")
print(f"   Сумма чисел до кортежа: {sum_before_tuple}")

# Задание 10
print("\n10. Операции с кортежами:")
# a) Проверка наличия элемента
search_tuple = (10, 20, 30, 20, 40, 50, 20)
search_element = 20
count_occurrences = search_tuple.count(search_element)
print(f"a) Кортеж: {search_tuple}")
print(f"   Элемент {search_element} встречается {count_occurrences} раз(а)")

# b) Преобразование списка в кортеж без дубликатов
string_list = ["яблоко", "банан", "яблоко", "апельсин", "банан", "вишня"]
unique_tuple = tuple(set(string_list))
print(f"б) Исходный список: {string_list}")
print(f"   Кортеж без дубликатов: {unique_tuple}")

# Задание 11
print("\n11. Операции с кортежами:")
# a) Преобразование списка в кортеж
user_list = [5, 10, 15, 20, 25]
converted_tuple = tuple(user_list)
print(f"a) Список: {user_list}")
print(f"   Кортеж: {converted_tuple}")

# b) Перемножение четных чисел
numbers_tuple = (2, 3, 4, 5, 6, 7, 8)
product = 1
even_numbers = [x for x in numbers_tuple if x % 2 == 0]
for num in even_numbers:
    product *= num
print(f"б) Кортеж чисел: {numbers_tuple}")
print(f"   Четные числа: {even_numbers}")
print(f"   Произведение четных: {product}")

# Задание 12
print("\n12. Операции с кортежами:")
# a) Удаление элемента из кортежа
original_tuple = (10, 20, 30, 40, 50)
element_to_remove = 30
filtered_tuple = tuple(x for x in original_tuple if x != element_to_remove)
print(f"a) Исходный кортеж: {original_tuple}")
print(f"   После удаления {element_to_remove}: {filtered_tuple}")

# b) Среднее значение чисел > 5 в кортежах
tuple_of_tuples = ((1, 6, 8), (3, 10, 15), (2, 4, 12), (7, 9, 11))
averages = []
for tup in tuple_of_tuples:
    numbers_gt_5 = [x for x in tup if isinstance(x, (int, float)) and x > 5]
    if numbers_gt_5:
        avg = sum(numbers_gt_5) / len(numbers_gt_5)
        averages.append(avg)
print(f"б) Кортеж кортежей: {tuple_of_tuples}")
print(f"   Средние значения чисел > 5: {averages}")

# Задание 13
print("\n13. Операции с кортежами:")
# a) Срез без строк
mixed_tuple = (1, "текст", 3.14, 5, "строка", 7, 8.5)
start, end = 1, 6  # срез от индекса 1 до 5
sliced = mixed_tuple[start:end]
numbers_only = tuple(x for x in sliced if not isinstance(x, str))
print(f"a) Исходный кортеж: {mixed_tuple}")
print(f"   Срез [{start}:{end}]: {sliced}")
print(f"   Без строк: {numbers_only}")

# b) Преобразование строк в целые числа
string_tuple = ("10", "-5", "25", "abc", "30", "-8")
converted_numbers = []
for s in string_tuple:
    try:
        num = int(s)
        if num >= 0:
            converted_numbers.append(num)
    except ValueError:
        continue
print(f"б) Строковый кортеж: {string_tuple}")
print(f"   Целочисленный кортеж: {tuple(converted_numbers)}")

# Задание 14
print("\n14. Операции с кортежами:")
# a) Поиск порядкового номера числового элемента
number_tuple = (10, "текст", 25, 3.14, 40, "строка", 55)
search_number = 25
number_indices = []
for i, item in enumerate(number_tuple, 1):
    if isinstance(item, (int, float)) and item == search_number:
        number_indices.append(i)
print(f"a) Кортеж: {number_tuple}")
print(f"   Элемент {search_number} имеет порядковый номер(а): {number_indices}")

# b) Объединение чисел кратных 3
numbers_tuple = (3, 6, 9, 12, 15, 2, 4, 18)
multiples_of_3 = [str(x) for x in numbers_tuple if x % 3 == 0]
if multiples_of_3:
    big_number = int(''.join(multiples_of_3))
else:
    big_number = 0
print(f"б) Кортеж чисел: {numbers_tuple}")
print(f"   Числа кратные 3: {multiples_of_3}")
print(f"   Объединенное число: {big_number}")

# Задание 15
print("\n15. Операции с кортежами:")
# a) Длина кортежа строк
mixed_tuple = ("привет", 123, "мир", 45.6, "python", True)
string_elements = [item for item in mixed_tuple if isinstance(item, str)]
string_length = len(string_elements)
print(f"a) Кортеж: {mixed_tuple}")
print(f"   Строковые элементы: {string_elements}")
print(f"   Количество строковых элементов: {string_length}")

# b) Поиск элемента в кортеже кортежей
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 2, 3))
search_item = 3
count_in_nested = 0
for tup in nested_tuple:
    count_in_nested += tup.count(search_item)
print(f"б) Кортеж кортежей: {nested_tuple}")
print(f"   Элемент {search_item} встречается {count_in_nested} раз(а)")
