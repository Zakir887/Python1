# Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в
# которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого
# меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
#
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.

s = input()
s = s.split()
n = int(s[0])
m = int(s[1])
a = []
for u in range(n):
    a.append([int(m) for m in input().split()])

max = a[0][0]
ind_i = 0
ind_j = 0
x = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        x = a[i][j]
        if int(x) > max:
            ind_i = i
            ind_j = j
            max = x
print(ind_i, ind_j)