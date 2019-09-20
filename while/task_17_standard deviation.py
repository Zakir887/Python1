# Дана последовательность натуральных чисел x1, x2, ..., xn.
# Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.

from math import sqrt

sx, sx2, n, x = 0, 0, 0, 0
x = int(input())
while x != 0:
    n += 1
    sx += x
    sx2 += x ** 2
    x = int(input())
print(sqrt((sx2 - sx ** 2 / n) / (n - 1)))
