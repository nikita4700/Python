from collections import Counter, defaultdict
import itertools
import math

print("ОПЕРАЦИИ СО СЛОВАРЯМИ")
print("=" * 50)

# Задание 1
print("\n1. Операции со словарями:")
dict1 = {1:2, 3:4, 4:3, 2:1, 0:0}

# a) Сортировка по значениям
sorted_asc = dict(sorted(dict1.items(), key=lambda x: x[1]))
sorted_desc = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
print(f"a) Сортировка по возрастанию: {sorted_asc}")
print(f"   Сортировка по убыванию: {sorted_desc}")

# b) Объединение с суммированием
dict1b = {1:2, 3:4}
dict2b = {3:5, 6:7}
merged = dict1b.copy()
for key, value in dict2b.items():
    merged[key] = merged.get(key, 0) + value
print(f"б) Объединение с суммированием: {merged}")

# c) Проверка наличия ключей
dict1c = {1:2, 3:4}
keys_to_check = [1, 3]
all_exist = all(key in dict1c for key in keys_to_check)
print(f"в) Все ключи {keys_to_check} присутствуют: {all_exist}")

# Задание 2
print("\n2. Операции со словарями:")
dict2 = {1:2, 3:4}

# a) Добавление ключа
dict2a = dict2.copy()
dict2a[5] = 6
print(f"a) После добавления ключа 5:6: {dict2a}")

# b) Уникальные значения
dict2b = {1:2, 3:4, 5:2}
unique_values = set(dict2b.values())
print(f"б) Уникальные значения: {unique_values}")

# c) Подсчет элементов в списках-значениях
dict2c = {1: [2, 3], 3: [5, 6, 7], 5: [8, 9, 10]}
total_elements = sum(len(lst) for lst in dict2c.values())
print(f"в) Всего элементов в списках: {total_elements}")

# Задание 3
print("\n3. Операции со словарями:")
# a) Объединение словарей
dicts_to_merge = [{1:2}, {3:4}, {5:6}]
merged_dict = {}
for d in dicts_to_merge:
    merged_dict.update(d)
print(f"a) Объединенный словарь: {merged_dict}")

# b) Сортировка по значениям
dict3b = {1:2, 3:4, 4:3, 2:1, 0:0}
sorted_dict = dict(sorted(dict3b.items(), key=lambda x: x[1]))
print(f"б) Отсортированный по значениям: {sorted_dict}")

# c) Очистка списков
dict3c = {1: [2, 3], 3: [5, 6, 7], 5: [8, 9, 10]}
cleaned_dict = {key: len(lst) for key, lst in dict3c.items()}
print(f"в) После очистки списков: {cleaned_dict}")

# Задание 4
print("\n4. Операции со словарями:")
# a) Проверка наличия ключей
dict4a = {1:2, 3:4}
keys_to_check = [1, 3]
all_exist = all(key in dict4a for key in keys_to_check)
print(f"a) Все ключи {keys_to_check} присутствуют: {all_exist}")

# b) Генерация комбинаций
dict4b = {1: 'abc', 2: 'def'}
key_to_permute = 1
if key_to_permute in dict4b:
    permutations = [''.join(p) for p in itertools.permutations(dict4b[key_to_permute])]
    print(f"б) Комбинации для ключа {key_to_permute}: {permutations}")

# c) Среднее значение
dict4c = {1: [2, 3, 4], 3: [5, 6, 7], 5: [8, 9, 0]}
averages = {key: sum(lst)/len(lst) for key, lst in dict4c.items()}
print(f"в) Средние значения: {averages}")

# Задание 5
print("\n5. Операции со словарями:")
dict5 = {1:2, 3:4, 5:6}

# a) Обход словаря
print("a) Обход словаря:")
for key, value in dict5.items():
    print(f"   Ключ: {key}, Значение: {value}")

# b) Три наибольших значения
top_three = sorted(dict5.values(), reverse=True)[:3]
print(f"б) Три наибольших значения: {top_three}")

# c) Сравнение значений
dict5c1 = {1:2, 3:4}
dict5c2 = {1:3, 3:4}
comparison = {key: (dict5c1.get(key), dict5c2.get(key)) for key in set(dict5c1) | set(dict5c2)}
print(f"в) Сравнение значений: {comparison}")

# Задание 6
print("\n6. Операции со словарями:")
# a) Словарь квадратов
n = 5
squares_dict = {i: i**2 for i in range(1, n+1)}
print(f"a) Словарь квадратов: {squares_dict}")

# b) Объединение значений в список
dict6b = {1:2, 3:4, 5:6}
values_list = list(dict6b.values())
print(f"б) Список значений: {values_list}")

# c) Удаление пустых элементов
dict6c = {1: '', 2: 'abc', 3: None, 4: [], 5: 'def'}
cleaned = {k: v for k, v in dict6c.items() if v not in ['', None, []]}
print(f"в) После удаления пустых: {cleaned}")

# Задание 7
print("\n7. Операции со словарями:")
# a) Словарь квадратов от 1 до 15
squares_15 = {i: i**2 for i in range(1, 16)}
print(f"a) Квадраты 1-15: {squares_15}")

# b) Частоты символов
text = "hello world"
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print(f"б) Частоты символов: {char_freq}")

# c) Фильтрация по значениям
dict7c = {'a':1, 'b':2, 'c':3, 'd':4}
filtered = {k: v for k, v in dict7c.items() if v > 2}
print(f"в) Отфильтрованный словарь: {filtered}")

# Задание 8
print("\n8. Операции со словарями:")
# a) Объединение словарей
dict8a1 = {'a':1, 'b':2}
dict8a2 = {'c':3, 'd':4}
merged8 = {**dict8a1, **dict8a2}
print(f"a) Объединенный словарь: {merged8}")

# b) Вывод в виде таблицы
dict8b = {'a':1, 'b':2, 'c':3, 'd':4}
print("б) Таблица:")
for key, value in dict8b.items():
    print(f"   {key} {value}")

# c) Преобразование списков в словарь
list1 = [1, 2, 3]
list2 = [4, 5, 6]
dict8c = {'key1': list1, 'key2': list2}
print(f"в) Словарь из списков: {dict8c}")

# Задание 9
print("\n9. Операции со словарями:")
# a) Обход словаря
dict9a = {'a':1, 'b':2, 'c':3, 'd':4}
print("a) Обход словаря:")
for key, value in dict9a.items():
    print(f"   key: {key}, value: {value}")

# b) Сумма значений по ключу
dict_list = [{'a': 1}, {'a': 2}, {'a': 3}, {'b': 1}]
sum_a = sum(d.get('a', 0) for d in dict_list)
print(f"б) Сумма значений по ключу 'a': {sum_a}")

# c) Фильтрация данных учащихся
students = {"Иван": {'рост':170, 'вес':70}, 'Михаил': {'рост':180, 'вес':75}}
filtered_students = {name: {'рост': data['рост']} for name, data in students.items()}
print(f"в) Отфильтрованные данные: {filtered_students}")

# Задание 10
print("\n10. Операции со словарями:")
# a) Сумма значений
dict10a = {'a':1, 'b':2, 'c':3, 'd':4}
total_sum = sum(dict10a.values())
print(f"a) Сумма всех значений: {total_sum}")

# b) Преобразование списка в словарь
list10b = ['a', 'b', 'c']
dict10b = {item: {} for item in list10b}
print(f"б) Словарь с пустыми значениями: {dict10b}")

# c) Проверка одинаковых значений
dict10c1 = {'a':1, 'b':1, 'c':1}
dict10c2 = {'a':1, 'b':2, 'c':1}
all_same1 = len(set(dict10c1.values())) == 1
all_same2 = len(set(dict10c2.values())) == 1
print(f"в) Все значения одинаковы в dict10c1: {all_same1}")
print(f"   Все значения одинаковы в dict10c2: {all_same2}")

# Задание 11
print("\n11. Операции со словарями:")
# a) Произведение значений
dict11a = {'a':1, 'b':2, 'c':3, 'd':4}
product = math.prod(dict11a.values())
print(f"a) Произведение всех значений: {product}")

# b) Сортировка списков значений
dict11b = {'a': ['c', 'b', 'a'], 'b': ['c', 'b', 'a']}
sorted_dict = {key: sorted(lst) for key, lst in dict11b.items()}
print(f"б) Отсортированные списки: {sorted_dict}")

# c) Группировка по ключам
pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)
print(f"в) Сгруппированные значения: {dict(grouped)}")

# Задание 12
print("\n12. Операции со словарями:")
# a) Удаление ключа
dict12a = {'a':1, 'b':2, 'c':3}
key_to_remove = 'b'
dict12a_copy = dict12a.copy()
dict12a_copy.pop(key_to_remove, None)
print(f"a) После удаления ключа '{key_to_remove}': {dict12a_copy}")

# b) Удаление пробелов из ключей (если бы они были)
dict12b = {'a ': 1, ' b': 2, 'c ': 3}
cleaned_keys = {key.strip(): value for key, value in dict12b.items()}
print(f"б) После удаления пробелов: {cleaned_keys}")

# c) Преобразование в список словарей
dict12c = {'a': [1, 2], 'b': [3, 4]}
result_list = []
for key, values in dict12c.items():
    for value in values:
        result_list.append({key: value})
print(f"в) Список словарей: {result_list}")

# Задание 13
print("\n13. Операции со словарями:")
# a) Объединение списков в словарь
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict13a = dict(zip(keys, values))
print(f"a) Словарь из списков: {dict13a}")

# b) Три самых дорогих товара
items = [
    {'name': 'item1', 'price': 10},
    {'name': 'item2', 'price': 50},
    {'name': 'item3', 'price': 30},
    {'name': 'item4', 'price': 40}
]
top_three_items = sorted(items, key=lambda x: x['price'], reverse=True)[:3]
print(f"б) Три самых дорогих товара: {top_three_items}")

# c) Удаление словаря из списка
dict_list13 = [{'a': 1}, {'b': 2}, {'c': 3}]
dict_to_remove = {'b': 2}
filtered_list = [d for d in dict_list13 if d != dict_to_remove]
print(f"в) После удаления {dict_to_remove}: {filtered_list}")

# Задание 14
print("\n14. Операции со словарями:")
# a) Сортировка по ключам
dict14a = {'b': 1, 'a': 2, 'c': 3}
sorted_by_key = dict(sorted(dict14a.items()))
print(f"a) Отсортированный по ключам: {sorted_by_key}")

# b) Извлечение ключей, значений и элементов
dict14b = {'a': 1, 'b': 2, 'c': 3}
print("б) Элементы словаря:")
for key, value in dict14b.items():
    print(f"   key: {key}, value: {value}, item: ({key}, {value})")

# c) Преобразование строк в числа
dict14c = {'a': '1', 'b': '2', 'c': '3.0'}
converted_dict = {}
for key, value in dict14c.items():
    try:
        if '.' in value:
            converted_dict[key] = float(value)
        else:
            converted_dict[key] = int(value)
    except ValueError:
        converted_dict[key] = value
print(f"в) После преобразования: {converted_dict}")

# Задание 15
print("\n15. Операции со словарями:")
# a) Максимальное и минимальное значение
dict15a = {'a': 1, 'b': 2, 'c': 3}
max_val = max(dict15a.values())
min_val = min(dict15a.values())
print(f"a) Максимальное значение: {max_val}, Минимальное значение: {min_val}")

# b) Вывод ключей и значений
dict15b = {'a': 1, 'b': 2, 'c': 3}
print("б) Ключи и значения:")
for key, value in dict15b.items():
    print(f"   key: {key}, value: {value}")

# c) Словарь с диапазонами
dict15c = {
    'x': list(range(11, 21)),
    'y': list(range(21, 31)),
    'z': list(range(31, 41))
}
print("в) Пятые элементы:")
for key, values in dict15c.items():
    print(f"   {key}: пятый элемент = {values[4]}")
