from collections import Counter, OrderedDict
import string

print("ОПЕРАЦИИ СО СТРОКАМИ - ЧАСТЬ 2")
print("=" * 50)

# Задание 1
print("1. Частоты символов в строке:")
s1 = "программирование"
freq = Counter(s1)
print(f"Строка: '{s1}'")
print("Частоты символов:")
for char, count in freq.items():
    print(f"  '{char}': {count}")

# Задание 2
print("\n2. Первые два и последние два символа:")
s2 = "Python"
if len(s2) >= 2:
    result2 = s2[:2] + s2[-2:]
    print(f"Строка: '{s2}'")
    print(f"Результат: '{result2}'")
else:
    print(f"Строка '{s2}' слишком короткая (меньше 2 символов)")

# Задание 3
print("\n3. Замена первого символа на $ (кроме самого первого):")
s3 = "программа"
first_char = s3[0]
result3 = first_char + s3[1:].replace(first_char, '$')
print(f"Строка: '{s3}'")
print(f"Результат: '{result3}'")

# Задание 4
print("\n4. Обмен первыми двумя символами двух строк:")
str1, str2 = "abc", "xyz"
result4 = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print(f"Строки: '{str1}', '{str2}'")
print(f"Результат: '{result4}'")

# Задание 5
print("\n5. Добавление 'ing' или 'ly':")
test_strings = ["read", "reading", "go", "abc"]
for s in test_strings:
    if len(s) >= 3:
        if s.endswith("ing"):
            result5 = s + "ly"
        else:
            result5 = s + "ing"
    else:
        result5 = s
    print(f"'{s}' -> '{result5}'")

# Задание 6
print("\n6. Удаление каждого n-го символа:")
s6 = "abcdefghijk"
n = 3
result6 = ''.join(s6[i] for i in range(len(s6)) if (i + 1) % n != 0)
print(f"Строка: '{s6}', n = {n}")
print(f"Результат: '{result6}'")

# Задание 7
print("\n7. Поменять местами первый и последний символы:")
s7 = "программа"
if len(s7) > 1:
    result7 = s7[-1] + s7[1:-1] + s7[0]
else:
    result7 = s7
print(f"Строка: '{s7}'")
print(f"Результат: '{result7}'")

# Задание 8
print("\n8. Удалить символы с нечетными индексами:")
s8 = "программирование"
result8 = s8[::2]  # символы с четными индексами (0, 2, 4...)
print(f"Строка: '{s8}'")
print(f"Результат: '{result8}'")

# Задание 9
print("\n9. Вхождение каждого слова в предложении:")
s9 = "кот собака кот птица собака кот"
words = s9.split()
word_count = Counter(words)
print(f"Предложение: '{s9}'")
print("Количество вхождений каждого слова:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# Задание 10
print("\n10. Перевернуть строку, если ее длина кратна 4:")
test_strings_10 = ["abcd", "python", "12345678", "test"]
for s in test_strings_10:
    if len(s) % 4 == 0:
        result10 = s[::-1]
    else:
        result10 = s
    print(f"'{s}' (длина {len(s)}) -> '{result10}'")

# Задание 11
print("\n11. Верхний регистр, если >=2 заглавных в первых 4 символах:")
test_strings_11 = ["ABcd", "AbCd", "abcd", "ABCd"]
for s in test_strings_11:
    first_four = s[:4]
    upper_count = sum(1 for char in first_four if char.isupper())
    if upper_count >= 2:
        result11 = s.upper()
    else:
        result11 = s
    print(f"'{s}' (заглавных в первых 4: {upper_count}) -> '{result11}'")

# Задание 12
print("\n12. Циклическая замена букв на следующие в алфавите:")
def shift_letters(text):
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    result.append('a')
                elif char == 'я':
                    result.append('а')
                else:
                    result.append(chr(ord(char) + 1))
            else:
                if char == 'Z':
                    result.append('A')
                elif char == 'Я':
                    result.append('А')
                else:
                    result.append(chr(ord(char) + 1))
        else:
            result.append(char)
    return ''.join(result)

s12 = "Hello World! Привет Мир!"
result12 = shift_letters(s12)
print(f"Исходная: '{s12}'")
print(f"Зашифрованная: '{result12}'")

# Задание 13
print("\n13. Первый неповторяющийся символ:")
def first_non_repeating_char(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

s13 = "программирование"
result13 = first_non_repeating_char(s13)
print(f"Строка: '{s13}'")
print(f"Первый неповторяющийся символ: '{result13}'")

# Задание 14
print("\n14. Верхний регистр для первой и последней буквы каждого слова:")
s14 = "привет мир программирование"
words = s14.split()
result_words = []
for word in words:
    if len(word) > 1:
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        new_word = word.upper()
    result_words.append(new_word)
result14 = ' '.join(result_words)
print(f"Исходная: '{s14}'")
print(f"Результат: '{result14}'")

# Задание 15
print("\n15. Проверка упорядоченности букв по алфавиту:")
def check_alphabet_order(s):
    letters = [char for char in s if char.isalpha() and char.islower()]
    for i in range(1, len(letters)):
        if letters[i] < letters[i-1]:
            # Находим позицию в исходной строке
            for j, char in enumerate(s):
                if char == letters[i]:
                    return j + 1
    return 0

test_strings_15 = ["abcde", "abdc", "python", "abcdef"]
for s in test_strings_15:
    result15 = check_alphabet_order(s)
    print(f"'{s}' -> {result15}")
