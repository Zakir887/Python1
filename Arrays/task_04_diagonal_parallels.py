# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть
# записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(len(a)):
        a[i][j] = abs(i - j)
for row in a:
    print(' '.join([str(elem) for elem in row]))