# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.

s = input()
s = s.split()
n = int(s[0])
m = int(s[1])
a = []
for i in range(n):
    a.append(['.'] * m)
for i in range(len(a)):
    x = 0
    if i%2 != 0:
        x +=1
    for j in range(len(a[i])):
        if x%2 == 0:
            a[i][j] = '.'
        else:
            a[i][j] = '*'
        x += 1
for row in a:
    print(' '.join([str(elem) for elem in row]))