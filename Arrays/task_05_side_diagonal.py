# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, n - i):
        a[i][j] = 1
    for j in range(0, n-i-1):
        a[i][j] = 0
    for j in range(n-i, n):
        a[i][j] = 2
for row in a:
    print(' '.join([str(elem) for elem in row]))