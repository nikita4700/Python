import math

# Общие параметры
x = 2
a = 3
b = 4

print("Значения функций при x = 2, a = 3, b = 4:")
print("=" * 50)

# 1. y = 3x^2 + sin(x + 2)
y1 = 3*x**2 + math.sin(x + 2)
print(f"1. y = {y1:.4f}")

# 2. y = ax^2 + cos(2x + 1)
y2 = a*x**2 + math.cos(2*x + 1)
print(f"2. y = {y2:.4f}")

# 3. y = ax + b*sin(2x + 2)
y3 = a*x + b*math.sin(2*x + 2)
print(f"3. y = {y3:.4f}")

# 4. y = ax^3 + cos(3x + 1)
y4 = a*x**3 + math.cos(3*x + 1)
print(f"4. y = {y4:.4f}")

# 5. y = x^2/a + cos(2x - 1)
y5 = x**2/a + math.cos(2*x - 1)
print(f"5. y = {y5:.4f}")

# 6. y = x/a + 2x^2
y6 = x/a + 2*x**2
print(f"6. y = {y6:.4f}")

# 7. y = 3x^2 - 2x + 1
y7 = 3*x**2 - 2*x + 1
print(f"7. y = {y7:.4f}")

# 8. y = (1/2)x^2 - 3x + 1
y8 = 0.5*x**2 - 3*x + 1
print(f"8. y = {y8:.4f}")

# 9. y = 1/(x^2 + 1) - a
y9 = 1/(x**2 + 1) - a
print(f"9. y = {y9:.4f}")

# 10. y = a/(x^2 + 1) - cos(2x - 1)
y10 = a/(x**2 + 1) - math.cos(2*x - 1)
print(f"10. y = {y10:.4f}")

# 11. y = x^3 - 2x^2 + 4
y11 = x**3 - 2*x**2 + 4
print(f"11. y = {y11:.4f}")

# 12. y = ax^2 + bx^3 - 8
y12 = a*x**2 + b*x**3 - 8
print(f"12. y = {y12:.4f}")

# 13. y = a*sqrt(x^2 + 4) - b
y13 = a*math.sqrt(x**2 + 4) - b
print(f"13. y = {y13:.4f}")

# 14. y = cos(2x - 1) + sin(x)
y14 = math.cos(2*x - 1) + math.sin(x)
print(f"14. y = {y14:.4f}")

# 15. y = a*sqrt(x) + b*x^2
y15 = a*math.sqrt(x) + b*x**2
print(f"15. y = {y15:.4f}")
