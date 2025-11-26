import math

print("=" * 60)
print("ЗАДАНИЕ 1: Среднее арифметическое и геометрическое")
print("=" * 60)

def Mean(X, Y):
    arithmetic_mean = (X + Y) / 2
    geometric_mean = math.sqrt(X * Y)
    return arithmetic_mean, geometric_mean

result = Mean(4, 9)
print(f"Mean(4, 9) = {result}")
print(f"Среднее арифметическое: {result[0]}")
print(f"Среднее геометрическое: {result[1]:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Площадь и длина окружности")
print("=" * 60)

def Circle(R):
    area = math.pi * R ** 2
    circumference = 2 * math.pi * R
    return area, circumference

result = Circle(5)
print(f"Circle(5) = {result}")
print(f"Площадь: {result[0]:.2f}")
print(f"Длина окружности: {result[1]:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Периметр и площадь равностороннего треугольника")
print("=" * 60)

def TrianglePS(a):
    P = 3 * a
    S = (math.sqrt(3) / 4) * a ** 2
    return P, S

result = TrianglePS(6)
print(f"TrianglePS(6) = {result}")
print(f"Периметр: {result[0]}")
print(f"Площадь: {result[1]:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Площадь кольца")
print("=" * 60)

def RingS(R1, R2):
    area = math.pi * (max(R1, R2) ** 2 - min(R1, R2) ** 2)
    return area

result = RingS(3, 5)
print(f"RingS(3, 5) = {result:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Периметр и площадь прямоугольника")
print("=" * 60)

def RectPS(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S

result = RectPS(1, 1, 4, 5)
print(f"RectPS(1, 1, 4, 5) = {result}")
print(f"Периметр: {result[0]}")
print(f"Площадь: {result[1]}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Периметр равнобедренного треугольника")
print("=" * 60)

def TriangleP(a, h):
    b = math.sqrt((a/2) ** 2 + h ** 2)
    P = a + 2 * b
    return P

result = TriangleP(6, 4)
print(f"TriangleP(6, 4) = {result:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Обратный порядок цифр")
print("=" * 60)

def InvertDigits(K):
    return int(str(K)[::-1])

result = InvertDigits(12345)
print(f"InvertDigits(12345) = {result}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Сумма чисел в диапазоне")
print("=" * 60)

def SumRange(A, B):
    if A > B:
        return 0
    return sum(range(A, B + 1))

result1 = SumRange(1, 5)
result2 = SumRange(5, 1)
print(f"SumRange(1, 5) = {result1}")
print(f"SumRange(5, 1) = {result2}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 9: Определение типа треугольника")
print("=" * 60)

def TypeTr(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    sides = [a, b, c]
    sides.sort()
    
    is_right = abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-9
    is_equilateral = abs(a - b) < 1e-9 and abs(b - c) < 1e-9
    is_isosceles = (abs(a - b) < 1e-9 or abs(b - c) < 1e-9 or abs(a - c) < 1e-9)
    
    if is_equilateral:
        return "равносторонний"
    elif is_right and is_isosceles:
        return "прямоугольный равнобедренный"
    elif is_right:
        return "прямоугольный"
    elif is_isosceles:
        return "равнобедренный"
    else:
        return "обычный"

result1 = TypeTr(0, 0, 3, 0, 0, 4)
result2 = TypeTr(0, 0, 2, 0, 1, math.sqrt(3))
print(f"TypeTr(0,0, 3,0, 0,4) = {result1}")
print(f"TypeTr(0,0, 2,0, 1,√3) = {result2}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 10: Номер координатной четверти")
print("=" * 60)

def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return "На оси координат"

result1 = Quarter(3, 4)
result2 = Quarter(-2, 5)
result3 = Quarter(-1, -1)
result4 = Quarter(2, -3)
print(f"Quarter(3, 4) = {result1}")
print(f"Quarter(-2, 5) = {result2}")
print(f"Quarter(-1, -1) = {result3}")
print(f"Quarter(2, -3) = {result4}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 11: Количество и сумма цифр числа")
print("=" * 60)

def DigitCountSum(K):
    digits = str(K)
    count = len(digits)
    total = sum(int(digit) for digit in digits)
    return count, total

result = DigitCountSum(12345)
print(f"DigitCountSum(12345) = {result}")
print(f"Количество цифр: {result[0]}")
print(f"Сумма цифр: {result[1]}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 12: Арифметические операции")
print("=" * 60)

def Calc(A, B, op):
    if op == 1:
        return A - B
    elif op == 2:
        return A * B
    elif op == 3:
        if B != 0:
            return A / B
        else:
            return "Ошибка: деление на ноль"
    else:
        return A + B

result1 = Calc(10, 5, 0)
result2 = Calc(10, 5, 1)
result3 = Calc(10, 5, 2)
result4 = Calc(10, 5, 3)
print(f"Calc(10, 5, 0) = {result1}")
print(f"Calc(10, 5, 1) = {result2}")
print(f"Calc(10, 5, 2) = {result3}")
print(f"Calc(10, 5, 3) = {result4}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 13: Счастливые номера")
print("=" * 60)

def LuckyNum(number):
    digits = str(number).zfill(4)
    first_sum = int(digits[0]) + int(digits[1])
    second_sum = int(digits[2]) + int(digits[3])
    return first_sum == second_sum

def getAllLuckyNumbers():
    return [num for num in range(1000, 10000) if LuckyNum(num)]

result1 = LuckyNum(1230)
result2 = LuckyNum(1234)
lucky_nums = getAllLuckyNumbers()[:10]
print(f"LuckyNum(1230) = {result1}")
print(f"LuckyNum(1234) = {result2}")
print(f"Первые 10 счастливых номеров: {lucky_nums}")
print(f"Всего счастливых номеров: {len(getAllLuckyNumbers())}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 14: Перевод градусов в радианы")
print("=" * 60)

def DegToRad(D):
    return D * math.pi / 180

result1 = DegToRad(180)
result2 = DegToRad(90)
result3 = DegToRad(45)
print(f"DegToRad(180) = {result1:.2f}")
print(f"DegToRad(90) = {result2:.2f}")
print(f"DegToRad(45) = {result3:.2f}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 15: Проверка високосного года")
print("=" * 60)

def IsLeapYear(Y):
    return (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0)

years = [2000, 2004, 1900, 2024, 2023]
for year in years:
    result = IsLeapYear(year)
    print(f"IsLeapYear({year}) = {result}")

print("\n" + "=" * 60)
print("=" * 60)
