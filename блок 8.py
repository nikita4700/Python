
# Создаем тестовую матрицу
matrix = [
    [1, 3, 5, 7, 9, 11],
    [2, 4, 6, 8, 10, 12],
    [9, 11, 13, 15, 17, 19],
    [10, 12, 14, 16, 18, 20],
    [21, 23, 25, 27, 29, 31],
    [22, 24, 26, 28, 30, 32]
]

print("Исходная матрица:")
for row in matrix:
    print(row)
print("\n" + "="*60 + "\n")

# 1. Первый столбец с только нечетными числами
result1 = 0
for j in range(len(matrix[0])):
    all_odd = True
    for i in range(len(matrix)):
        if matrix[i][j] % 2 == 0:
            all_odd = False
            break
    if all_odd:
        result1 = j + 1
        break
print(f"1. Первый столбец с только нечетными числами: {result1}")

# 2. Поменять min и max в каждой строке
result2 = [row[:] for row in matrix]
for i in range(len(result2)):
    min_val = min(result2[i])
    max_val = max(result2[i])
    min_idx = result2[i].index(min_val)
    max_idx = result2[i].index(max_val)
    result2[i][min_idx], result2[i][max_idx] = result2[i][max_idx], result2[i][min_idx]
print("2. Матрица после замены min и max в каждой строке:")
for row in result2:
    print(row)

# 3. Поменять строки с минимальным и максимальным элементами
result3 = [row[:] for row in matrix]
min_val = min(min(row) for row in result3)
max_val = max(max(row) for row in result3)
min_row = max_row = -1
for i in range(len(result3)):
    if min_val in result3[i]:
        min_row = i
    if max_val in result3[i]:
        max_row = i
if min_row != -1 and max_row != -1:
    result3[min_row], result3[max_row] = result3[max_row], result3[min_row]
print("3. Матрица после замены строк с min и max элементами:")
for row in result3:
    print(row)

# 4. Зеркально отразить относительно горизонтальной оси
result4 = [row[:] for row in matrix[::-1]]
print("4. Матрица после горизонтального отражения:")
for row in result4:
    print(row)

# 5. Удалить строку с минимальным элементом
result5 = [row[:] for row in matrix]
min_val = min(min(row) for row in result5)
min_row_index = -1
for i in range(len(result5)):
    if min_val in result5[i]:
        min_row_index = i
        break
if min_row_index != -1:
    del result5[min_row_index]
print("5. Матрица после удаления строки с минимальным элементом:")
for row in result5:
    print(row)

# 6. Удалить столбец с максимальным элементом
result6 = [row[:] for row in matrix]
max_val = max(max(row) for row in result6)
max_col_index = -1
for j in range(len(result6[0])):
    for i in range(len(result6)):
        if result6[i][j] == max_val:
            max_col_index = j
            break
    if max_col_index != -1:
        break
if max_col_index != -1:
    for i in range(len(result6)):
        del result6[i][max_col_index]
print("6. Матрица после удаления столбца с максимальным элементом:")
for row in result6:
    print(row)

# 7. Зеркально отразить относительно вертикальной оси
result7 = [row[::-1] for row in matrix]
print("7. Матрица после вертикального отражения:")
for row in result7:
    print(row)

# 8. Продублировать строку с максимальным элементом
result8 = [row[:] for row in matrix]
max_val = max(max(row) for row in result8)
max_row_index = -1
for i in range(len(result8)):
    if max_val in result8[i]:
        max_row_index = i
        break
if max_row_index != -1:
    result8.insert(max_row_index + 1, result8[max_row_index][:])
print("8. Матрица после дублирования строки с максимальным элементом:")
for row in result8:
    print(row)

# 9. Количество элементов больше среднего в каждом столбце
result9 = []
for j in range(len(matrix[0])):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    col_avg = col_sum / len(matrix)
    count = sum(1 for i in range(len(matrix)) if matrix[i][j] > col_avg)
    result9.append(count)
print(f"9. Количество элементов больше среднего в каждом столбце: {result9}")

# 10. Поменять левую верхнюю и правую нижнюю четверти
result10 = [row[:] for row in matrix]
m, n = len(result10), len(result10[0])
mid_m, mid_n = m // 2, n // 2
for i in range(mid_m):
    for j in range(mid_n):
        result10[i][j], result10[i + mid_m][j + mid_n] = result10[i + mid_m][j + mid_n], result10[i][j]
print("10. Матрица после замены левой верхней и правой нижней четвертей:")
for row in result10:
    print(row)

# 11. Среднее арифметическое для строк с нечетными номерами
result11 = {}
for i in range(0, len(matrix), 2):
    row_sum = sum(matrix[i])
    row_avg = row_sum / len(matrix[i])
    result11[i + 1] = row_avg
print(f"11. Среднее арифметическое для строк с нечетными номерами: {result11}")

# 12. Строка с наибольшей суммой элементов
max_sum = -1
max_row_num = -1
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    if row_sum > max_sum:
        max_sum = row_sum
        max_row_num = i + 1
print(f"12. Строка с наибольшей суммой: №{max_row_num}, сумма = {max_sum}")

# 13. Вставить строку нулей перед строкой с минимальным элементом
result13 = [row[:] for row in matrix]
min_val = min(min(row) for row in result13)
min_row_index = -1
for i in range(len(result13)):
    if min_val in result13[i]:
        min_row_index = i
        break
if min_row_index != -1:
    zeros_row = [0] * len(result13[0])
    result13.insert(min_row_index, zeros_row)
print("13. Матрица после вставки строки нулей перед строкой с min элементом:")
for row in result13:
    print(row)

# 14. Последняя строка с только четными числами
result14 = 0
for i in range(len(matrix) - 1, -1, -1):
    all_even = True
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 != 0:
            all_even = False
            break
    if all_even:
        result14 = i + 1
        break
print(f"14. Последняя строка с только четными числами: {result14}")

# 15. Поменять первый и последний положительный столбец
result15 = [row[:] for row in matrix]
positive_cols = []
for j in range(len(result15[0])):
    all_positive = True
    for i in range(len(result15)):
        if result15[i][j] <= 0:
            all_positive = False
            break
    if all_positive:
        positive_cols.append(j)
if len(positive_cols) >= 2:
    first_col = 0
    last_positive_col = positive_cols[-1]
    for i in range(len(result15)):
        result15[i][first_col], result15[i][last_positive_col] = result15[i][last_positive_col], result15[i][first_col]
print("15. Матрица после замены первого и последнего положительного столбца:")
for row in result15:
    print(row)
