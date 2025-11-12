import string

print("ОПЕРАЦИИ СО СТРОКАМИ")
print("=" * 50)

# Общие тестовые строки
s1 = "ПРИВЕТ   МИР   КАК   ДЕЛА"
s2 = "Анна   шалаш   дом   уровень   мадам"
s3 = "АРБУЗ   БАНАН   ВИШНЯ   ГРУША"
s4 = "это   тестовая   строка   с   разными   словами"
s5 = "Программа   для   обработки   строк"
s6 = "C:/Users/divivanov/primer/prog.py"

# Задание 1
print("1. Количество слов в строке:")
words1 = s1.split()
print(f"Строка: '{s1}'")
print(f"Количество слов: {len(words1)}")

# Задание 2
print("\n2. Слова, начинающиеся и заканчивающиеся одной буквой:")
words2 = s2.split()
count2 = sum(1 for word in words2 if word and word[0].upper() == word[-1].upper())
print(f"Строка: '{s2}'")
print(f"Количество слов: {count2}")
print(f"Слова: {[word for word in words2 if word and word[0].upper() == word[-1].upper()]}")

# Задание 3
print("\n3. Слова, содержащие букву 'А':")
words3 = s3.split()
count3 = sum(1 for word in words3 if 'А' in word)
print(f"Строка: '{s3}'")
print(f"Количество слов: {count3}")
print(f"Слова: {[word for word in words3 if 'А' in word]}")

# Задание 4
print("\n4. Длина самого короткого слова:")
words4 = s4.split()
min_len = min(len(word) for word in words4) if words4 else 0
print(f"Строка: '{s4}'")
print(f"Длина самого короткого слова: {min_len}")
print(f"Самое короткое слово: {[word for word in words4 if len(word) == min_len]}")

# Задание 5
print("\n5. Слова в обратном порядке:")
words5 = s5.split()
reversed_words = ' '.join(reversed(words5))
print(f"Строка: '{s5}'")
print(f"Результат: '{reversed_words}'")

# Задание 6
print("\n6. Слова в алфавитном порядке:")
words6 = s3.split()
sorted_words = ' '.join(sorted(words6))
print(f"Строка: '{s3}'")
print(f"Результат: '{sorted_words}'")

# Задание 7
print("\n7. Вставка строки перед символом C:")
C = 'а'
S = "банан ананас арбуз"
S0 = "ФРУКТ"
result7 = S0.join(S.split(C))
print(f"Символ C: '{C}'")
print(f"Строка S: '{S}'")
print(f"Строка S0: '{S0}'")
print(f"Результат: '{result7}'")

# Задание 8
print("\n8. Удаление избыточных пробелов:")
s8 = "   это   строка   с   лишними   пробелами   "
result8 = ' '.join(s8.split())
print(f"Исходная строка: '{s8}'")
print(f"Результат: '{result8}'")

# Задание 9
print("\n9. Количество строчных латинских и русских букв:")
s9 = "Hello Мир Test 123 Привет!"
latin_lower = sum(1 for char in s9 if char in string.ascii_lowercase)
russian_lower = sum(1 for char in s9 if 'а' <= char <= 'я')
total_lower = latin_lower + russian_lower
print(f"Строка: '{s9}'")
print(f"Строчных латинских букв: {latin_lower}")
print(f"Строчных русских букв: {russian_lower}")
print(f"Всего строчных букв: {total_lower}")

# Задание 10
print("\n10. Длина самого длинного слова:")
words10 = s4.split()
max_len = max(len(word) for word in words10) if words10 else 0
print(f"Строка: '{s4}'")
print(f"Длина самого длинного слова: {max_len}")
print(f"Самое длинное слово: {[word for word in words10 if len(word) == max_len]}")

# Задание 11
print("\n11. Шифрование строки:")
s11 = "Программа"
even_chars = s11[1::2]  # символы на четных позициях
odd_chars = s11[0::2]   # символы на нечетных позициях
result11 = even_chars + odd_chars[::-1]
print(f"Исходная строка: '{s11}'")
print(f"Четные позиции: '{even_chars}'")
print(f"Нечетные позиции: '{odd_chars}'")
print(f"Результат: '{result11}'")

# Задание 12
print("\n12. Вставка звездочек между символами:")
S = "Python"
N = 3
stars = '*' * N
result12 = stars.join(S)
print(f"Строка S: '{S}'")
print(f"Число N: {N}")
print(f"Результат: '{result12}'")

# Задание 13
print("\n13. Разделение слов точками:")
words13 = s4.split()
result13 = '.'.join(words13)
print(f"Строка: '{s4}'")
print(f"Результат: '{result13}'")

# Задание 14
print("\n14. Имя файла без расширения:")
import os
filename = os.path.basename(s6)
name_without_ext = os.path.splitext(filename)[0]
print(f"Полный путь: '{s6}'")
print(f"Имя файла: '{filename}'")
print(f"Имя без расширения: '{name_without_ext}'")

# Задание 15
print("\n15. Самое длинное слово (последнее при равенстве):")
words15 = s4.split()
if words15:
    max_length = max(len(word) for word in words15)
    longest_word = next(word for word in reversed(words15) if len(word) == max_length)
else:
    longest_word = ""
print(f"Строка: '{s4}'")
print(f"Самое длинное слово: '{longest_word}'")
print(f"Его длина: {len(longest_word)}")
