import math

# Общие параметры
x = 2
a = 3

print("ВЫЧИСЛЕНИЕ КУСОЧНО-ЗАДАННЫХ ФУНКЦИЙ")
print(f"При x = {x}, a = {a}")
print("=" * 50)

# Задание 1
if x > 0:
    y1 = a*x**2 + 1
else:
    y1 = a*x - 1
print(f"1. y = {y1}")

# Задание 2
if x >= 1:
    y2 = a*x + 1
else:
    y2 = x**2 - 1
print(f"2. y = {y2}")

# Задание 3
if x < 0:
    y3 = 3*a**2
else:
    y3 = 4*a*x - 1
print(f"3. y = {y3}")

# Задание 4
if x > 4:
    y4 = 2*a**2
else:
    y4 = 3*x - 1
print(f"4. y = {y4}")

# Задание 5
if x > 2:
    y5 = 2*a*x - 2
else:
    y5 = 3*a**2 - 2*x
print(f"5. y = {y5}")

# Задание 6
if x > 1:
    y6 = 2*a*x**2 - 1
else:
    y6 = x
print(f"6. y = {y6}")

# Задание 7
if x > 2:
    y7 = x**2
else:
    y7 = 2*a - 1
print(f"7. y = {y7}")

# Задание 8
if x > 2:
    y8 = math.cos(2*x - 1)
else:
    y8 = math.sin(3*x + 1)
print(f"8. y = {y8:.4f}")

# Задание 9
if x > 2:
    y9 = 2*x**3 - 2*x - 1
else:
    y9 = 3*x**2 - 2*x + 1
print(f"9. y = {y9}")

# Задание 10
if x > 1:
    y10 = 2*a*x**2 - 1
else:
    y10 = 1/a
print(f"10. y = {y10:.4f}")

# Задание 11
if x >= 0:
    y11 = a*math.sqrt(x) + 1
else:
    y11 = a*x - 1
print(f"11. y = {y11:.4f}")

# Задание 12
if x >= 0:
    y12 = math.sqrt(x) + a
else:
    y12 = a/x - 1
print(f"12. y = {y12:.4f}")

# Задание 13
if x > 0:
    y13 = 1/x + a
else:
    y13 = x**2 - 1
print(f"13. y = {y13:.4f}")

# Задание 14
if x > math.pi/2:
    y14 = math.cos(x)
else:
    y14 = math.sin(x)
print(f"14. y = {y14:.4f}")

# Задание 15
if x > 2:
    y15 = math.sqrt(x - 2)
else:
    y15 = (x - 2)**2 + 1
print(f"15. y = {y15:.4f}")
