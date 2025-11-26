import numpy as np

print("=" * 60)
print("ЗАДАНИЕ 1: Удаление строки и столбца")
print("=" * 60)

def RemoveRowCol(A, K, L):
    if K >= len(A) or L >= len(A[0]):
        return A
    
    new_matrix = []
    for i in range(len(A)):
        if i != K:
            new_row = []
            for j in range(len(A[0])):
                if j != L:
                    new_row.append(A[i][j])
            new_matrix.append(new_row)
    return new_matrix

# Пример
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
result = RemoveRowCol(matrix, 1, 2)
print("Исходная матрица:")
for row in matrix:
    print(row)
print("После удаления строки 1, столбца 2:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Разделение на четные и нечетные")
print("=" * 60)

def Split(A):
    B = [x for x in A if x % 2 == 0]
    C = [x for x in A if x % 2 != 0]
    return B, C

# Пример
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B, C = Split(A)
print(f"Исходный список: {A}")
print(f"Четные: {B}")
print(f"Нечетные: {C}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Обмен строк")
print("=" * 60)

def SwapRow(A, K1, K2):
    if K1 < len(A) and K2 < len(A):
        A[K1], A[K2] = A[K2], A[K1]
    return A

# Пример
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = SwapRow(matrix, 0, 2)
print("После обмена строк 0 и 2:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Транспонирование")
print("=" * 60)

def Transp(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Пример
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = Transp(matrix)
print("После транспонирования:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Произведение матриц")
print("=" * 60)

def MtrProd(A, B):
    if len(A[0]) != len(B):
        return "Несовместимые размеры"
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Пример
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = MtrProd(A, B)
print("Матрица A:")
for row in A:
    print(row)
print("Матрица B:")
for row in B:
    print(row)
print("Произведение A×B:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Сумма матриц")
print("=" * 60)

def SumMtr(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Несовместимые размеры"
    
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Пример
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = SumMtr(A, B)
print("Матрица A:")
for row in A:
    print(row)
print("Матрица B:")
for row in B:
    print(row)
print("Сумма A+B:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Сумма диагоналей")
print("=" * 60)

def SumDiagonal(matrix, diagonal_type='main'):
    n = len(matrix)
    if diagonal_type == 'main':
        return sum(matrix[i][i] for i in range(n))
    else:  # побочная
        return sum(matrix[i][n-1-i] for i in range(n))

# Пример
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Матрица:")
for row in matrix:
    print(row)
print(f"Сумма главной диагонали: {SumDiagonal(matrix, 'main')}")
print(f"Сумма побочной диагонали: {SumDiagonal(matrix, 'side')}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Удаление диапазона строк")
print("=" * 60)

def RemoveRows(A, K1, K2):
    if K1 >= len(A):
        return A
    
    K2 = min(K2, len(A) - 1)
    return [A[i] for i in range(len(A)) if i < K1 or i > K2]

# Пример
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = RemoveRows(matrix, 1, 3)
print("После удаления строк 1-3:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 9: Инвертирование подстроки")
print("=" * 60)

def InvertStr(S, K, N):
    if K >= len(S):
        return ""
    
    end = min(K + N, len(S))
    substring = S[K:end]
    return S[:K] + substring[::-1] + S[end:]

# Пример
S = "Hello World!"
result1 = InvertStr(S, 6, 5)
result2 = InvertStr(S, 20, 5)  # K > длины строки
print(f"Исходная строка: '{S}'")
print(f"InvertStr('{S}', 6, 5) = '{result1}'")
print(f"InvertStr('{S}', 20, 5) = '{result2}'")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 10: Обмен столбцов")
print("=" * 60)

def SwapCol(A, K1, K2):
    if K1 >= len(A[0]) or K2 >= len(A[0]):
        return A
    
    for i in range(len(A)):
        A[i][K1], A[i][K2] = A[i][K2], A[i][K1]
    return A

# Пример
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = SwapCol(matrix, 1, 3)
print("После обмена столбцов 1 и 3:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 11: Сжатие строки")
print("=" * 60)

def CompressStr(S):
    if not S:
        return ""
    
    result = []
    count = 1
    current_char = S[0]
    
    for i in range(1, len(S)):
        if S[i] == current_char:
            count += 1
        else:
            if count > 4:
                result.append(current_char + f"({count})")
            else:
                result.append(current_char * count)
            current_char = S[i]
            count = 1
    
    # Обработка последней последовательности
    if count > 4:
        result.append(current_char + f"({count})")
    else:
        result.append(current_char * count)
    
    return "".join(result)

# Пример
S1 = "bbbccccc"
S2 = "aaaaabbbcccddddeeeee"
result1 = CompressStr(S1)
result2 = CompressStr(S2)
print(f"CompressStr('{S1}') = '{result1}'")
print(f"CompressStr('{S2}') = '{result2}'")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 12: Проверка идентификатора")
print("=" * 60)

def IsIdent(S):
    if not S or S[0].isdigit():
        return False
    
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    return all(char in valid_chars for char in S)

# Пример
identifiers = ["var_name", "2var", "_temp", "var-name", "Var123", ""]
for ident in identifiers:
    result = IsIdent(ident)
    print(f"IsIdent('{ident}') = {result}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 13: Шахматная доска")
print("=" * 60)

def Chessboard(M, N):
    return [[(i + j) % 2 for j in range(N)] for i in range(M)]

# Пример
result = Chessboard(4, 5)
print("Шахматная доска 4x5:")
for row in result:
    print(row)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 14: Колоколообразная сортировка")
print("=" * 60)

def Bell(L):
    sorted_L = sorted(L)
    result = []
    left, right = 0, len(sorted_L) - 1
    
    while left <= right:
        if left == right:
            result.append(sorted_L[left])
        else:
            result.append(sorted_L[left])
            result.append(sorted_L[right])
        left += 1
        right -= 1
    
    return result

# Пример
L = [5, 2, 8, 1, 9, 3]
result = Bell(L)
print(f"Исходный список: {L}")
print(f"После Bell: {result}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 15: Удаление диапазона столбцов")
print("=" * 60)

def RemoveCols(A, K1, K2):
    if K1 >= len(A[0]):
        return A
    
    K2 = min(K2, len(A[0]) - 1)
    result = []
    for i in range(len(A)):
        new_row = []
        for j in range(len(A[0])):
            if j < K1 or j > K2:
                new_row.append(A[i][j])
        result.append(new_row)
    return result

# Пример
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print("Исходная матрица:")
for row in matrix:
    print(row)
result = RemoveCols(matrix, 1, 3)
print("После удаления столбцов 1-3:")
for row in result:
    print(row)

