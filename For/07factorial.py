# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!. По данному натуральному n вычислите
# значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input())
c, f = 0, 1

for c in range(1, n+1):
	f *= c
print(f)