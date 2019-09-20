# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = [int(i) for i in input().split()]
x = 0  # max
y = 0  # min
for i in range(1, len(a)):
    if a[i - 1] < a[i]:
        if a[i] > a[x]:
            x = i
for i in range(1, len(a)):
    if a[i - 1] > a[i]:
        if a[i] < a[y]:
            y = i
a[x], a[y] = a[y], a[x]
print(' '.join([str(i) for i in a]))
