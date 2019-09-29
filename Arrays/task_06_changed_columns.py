# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).

def swap_columns(a, i, j):
    for s in range(n):
        a[s][i], a[s][j] = a[s][j], a[s][i]
    return a

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
if i > j:
    i, j = j, i

swap_columns(a, i, j)
for row in a:
        print(' '.join([str(elem) for elem in row]))