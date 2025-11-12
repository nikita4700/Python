import math

# Общие параметры
n = 5
x = 0.5

print("ВЫЧИСЛЕНИЕ СУММ РЯДОВ")
print(f"При n = {n}, x = {x}")
print("=" * 50)

# Задание 1
print("\n1. Сумма: 1/2 + 1/2² + 1/2³ + ... + 1/2ⁿ")
sum1 = sum(1/(2**i) for i in range(1, n+1))
print(f"Результат: {sum1:.6f}")

# Задание 2
print("\n2. Сумма: cos x + cos²x/2 + cos³x/3 + ... + cosⁿx/n")
sum2 = sum((math.cos(x)**i)/i for i in range(1, n+1))
print(f"Результат: {sum2:.6f}")

# Задание 3
print("\n3. Сумма: 1 - 3 + 3² - 3³ + ... + (-1)ⁿ·3ⁿ")
sum3 = sum((-1)**i * (3**i) for i in range(n+1))
print(f"Результат: {sum3}")

# Задание 4
print("\n4. Сумма: 1/sin 1 + 1/sin 2 + ... + 1/sin n")
sum4 = sum(1/math.sin(i) for i in range(1, n+1))
print(f"Результат: {sum4:.6f}")

# Задание 5
print("\n5. Сумма: 1 - 2³ + 3³ - ... + (-1)ⁿ⁺¹·n³")
sum5 = sum((-1)**(i+1) * (i**3) for i in range(1, n+1))
print(f"Результат: {sum5}")

# Задание 6
print("\n6. Сумма: cos 1 - cos 2 + cos 3 - ... + (-1)ⁿ⁺¹·cos n")
sum6 = sum((-1)**(i+1) * math.cos(i) for i in range(1, n+1))
print(f"Результат: {sum6:.6f}")

# Задание 7
print("\n7. Сумма: x - x²/2 + x³/3 - ... + (-1)ⁿ⁻¹·xⁿ/n")
sum7 = sum((-1)**(i-1) * (x**i)/i for i in range(1, n+1))
print(f"Результат: {sum7:.6f}")

# Задание 8
print("\n8. Сумма: 1! - 2! + 3! - ... + (-1)ⁿ⁺¹·n!")
def factorial(num):
    return 1 if num == 0 else num * factorial(num-1)

sum8 = sum((-1)**(i+1) * factorial(i) for i in range(1, n+1))
print(f"Результат: {sum8}")

# Задание 9
print("\n9. Сумма: sin x + sin x² + sin x³ + ... + sin xⁿ")
sum9 = sum(math.sin(x**i) for i in range(1, n+1))
print(f"Результат: {sum9:.6f}")

# Задание 10
print("\n10. Сумма: 1 + 1/2! + 1/3! + ... + 1/n!")
sum10 = sum(1/factorial(i) for i in range(1, n+1))
print(f"Результат: {sum10:.6f}")

# Задание 11
print("\n11. Сумма: n² + (n+1)² + (n+2)² + ... + (2n)²")
sum11 = sum((n+i)**2 for i in range(n+1))
print(f"Результат: {sum11}")

# Задание 12
print("\n12. Сумма: 1! + 2! + 3! + ... + n!")
sum12 = sum(factorial(i) for i in range(1, n+1))
print(f"Результат: {sum12}")

# Задание 13
print("\n13. Сумма: 1 + x + x²/2! + x³/3! + ... + xⁿ/n!")
sum13 = sum((x**i)/factorial(i) for i in range(n+1))
print(f"Результат: {sum13:.6f}")

# Задание 14
print("\n14. Сумма: 1 - x + x² - x³ + ... + (-1)ⁿ·xⁿ")
sum14 = sum((-1)**i * (x**i) for i in range(n+1))
print(f"Результат: {sum14:.6f}")

# Задание 15 (арксинус)
print("\n15. Сумма: x + x³/3 + x⁵/5 + ... + x²ⁿ⁺¹/(2n+1)")
sum15 = sum((x**(2*i+1))/(2*i+1) for i in range(n+1))
print(f"Результат: {sum15:.6f}")
print(f"Для сравнения: arctanh({x}) = {math.atanh(x):.6f}")
