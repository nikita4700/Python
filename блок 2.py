import math

print("РЕШЕНИЕ ЗАДАЧ 1-15")
print("=" * 50)

# Задача 1
print("\n1. Прямоугольный параллелепипед:")
a, b, c = 3, 4, 5
V = a * b * c
S = 2 * (a*b + b*c + a*c)
print(f"Дано: a={a}, b={b}, c={c}")
print(f"Объем V = {V}")
print(f"Площадь поверхности S = {S}")

# Задача 2
print("\n2. Окружность и круг:")
R = 7
L = 2 * math.pi * R
S_circle = math.pi * R**2
print(f"Дано: R={R}")
print(f"Длина окружности L = {L:.2f}")
print(f"Площадь круга S = {S_circle:.2f}")

# Задача 3
print("\n3. Прямоугольный треугольник:")
a_tri, b_tri = 6, 8
c_tri = math.sqrt(a_tri**2 + b_tri**2)
P_tri = a_tri + b_tri + c_tri
print(f"Дано: катеты a={a_tri}, b={b_tri}")
print(f"Гипотенуза c = {c_tri:.2f}")
print(f"Периметр P = {P_tri:.2f}")

# Задача 4
print("\n4. Два круга и кольцо:")
R1, R2 = 10, 6
S1 = math.pi * R1**2
S2 = math.pi * R2**2
S3 = S1 - S2
print(f"Дано: R1={R1}, R2={R2}")
print(f"Площадь большого круга S1 = {S1:.2f}")
print(f"Площадь малого круга S2 = {S2:.2f}")
print(f"Площадь кольца S3 = {S3:.2f}")

# Задача 5
print("\n5. Прямоугольник по координатам:")
x1, y1 = 1, 1
x2, y2 = 4, 5
width = abs(x2 - x1)
height = abs(y2 - y1)
P_rect = 2 * (width + height)
S_rect = width * height
print(f"Дано: ({x1},{y1}), ({x2},{y2})")
print(f"Стороны: {width} x {height}")
print(f"Периметр P = {P_rect}")
print(f"Площадь S = {S_rect}")

# Задача 6
print("\n6. Расстояние между точками:")
x1_p, y1_p = 2, 3
x2_p, y2_p = 8, 12
distance = math.sqrt((x2_p - x1_p)**2 + (y2_p - y1_p)**2)
print(f"Дано: A({x1_p},{y1_p}), B({x2_p},{y2_p})")
print(f"Расстояние AB = {distance:.2f}")

# Задача 7
print("\n7. Треугольник по координатам:")
x1_t, y1_t = 0, 0
x2_t, y2_t = 4, 0
x3_t, y3_t = 0, 3

def distance_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

a_side = distance_points(x1_t, y1_t, x2_t, y2_t)
b_side = distance_points(x2_t, y2_t, x3_t, y3_t)
c_side = distance_points(x3_t, y3_t, x1_t, y1_t)

P_triangle = a_side + b_side + c_side
p = P_triangle / 2
S_triangle = math.sqrt(p * (p - a_side) * (p - b_side) * (p - c_side))

print(f"Дано: A({x1_t},{y1_t}), B({x2_t},{y2_t}), C({x3_t},{y3_t})")
print(f"Стороны: a={a_side:.1f}, b={b_side:.1f}, c={c_side:.1f}")
print(f"Периметр P = {P_triangle:.2f}")
print(f"Площадь S = {S_triangle:.2f}")

# Задача 8
print("\n8. Перевод температуры:")
T_f = 100
T_c = (T_f - 32) * 5/9
print(f"Дано: {T_f}°F")
print(f"Температура в Цельсиях: {T_c:.1f}°C")

# Задача 9
print("\n9. Стоимость конфет:")
X, A = 2, 500  # 2 кг шоколадных за 500 руб
Y, B = 3, 240  # 3 кг ирисок за 240 руб

price_choc = A / X
price_iris = B / Y
ratio = price_choc / price_iris

print(f"Дано: {X} кг шоколадных = {A} руб, {Y} кг ирисок = {B} руб")
print(f"1 кг шоколадных: {price_choc:.1f} руб")
print(f"1 кг ирисок: {price_iris:.1f} руб")
print(f"Шоколадные дороже в {ratio:.1f} раз")

# Задача 10
print("\n10. Система уравнений:")
A1, B1, C1 = 2, 3, 7
A2, B2, C2 = 1, -1, 1

D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D

print(f"Система: {A1}x + {B1}y = {C1}")
print(f"         {A2}x + {B2}y = {C2}")
print(f"Решение: x = {x:.1f}, y = {y:.1f}")

# Задача 11
print("\n11. Перевод угла в радианы:")
alpha_deg = 180
alpha_rad = alpha_deg * math.pi / 180
print(f"Дано: {alpha_deg}°")
print(f"В радианах: {alpha_rad:.2f}")

# Задача 12
print("\n12. Расстояние между автомобилями:")
V1, V2 = 60, 80
S_start = 100
T = 2

S_end = S_start + (V1 + V2) * T
print(f"Дано: V1={V1} км/ч, V2={V2} км/ч, S={S_start} км, T={T} ч")
print(f"Расстояние через {T} ч: {S_end} км")

# Задача 13
print("\n13. Отрезки на числовой оси:")
A, B, C = 2, 8, 5
AC = abs(C - A)
BC = abs(C - B)
sum_AC_BC = AC + BC
print(f"Дано: A={A}, B={B}, C={C}")
print(f"Длина AC = {AC}")
print(f"Длина BC = {BC}")
print(f"Сумма AC + BC = {sum_AC_BC}")

# Задача 14
print("\n14. Операции с квадратами:")
num1, num2 = 4, 3
sum_sq = num1**2 + num2**2
diff_sq = num1**2 - num2**2
prod_sq = num1**2 * num2**2
quot_sq = num1**2 / num2**2
print(f"Дано: {num1}, {num2}")
print(f"Сумма квадратов: {sum_sq}")
print(f"Разность квадратов: {diff_sq}")
print(f"Произведение квадратов: {prod_sq}")
print(f"Частное квадратов: {quot_sq:.2f}")

# Задача 15
print("\n15. Путь лодки:")
V_boat = 12
U_river = 3
T1, T2 = 2, 3

S_lake = V_boat * T1
S_river = (V_boat - U_river) * T2
S_total = S_lake + S_river

print(f"Дано: V={V_boat} км/ч, U={U_river} км/ч")
print(f"Время по озеру: {T1} ч, против течения: {T2} ч")
print(f"Путь по озеру: {S_lake} км")
print(f"Путь по реке: {S_river} км")
print(f"Общий путь: {S_total} км")
