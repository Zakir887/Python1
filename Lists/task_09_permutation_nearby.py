# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний
# элемент остается на своем месте.

a = [i for i in input().split()]
n = int(len(a))
if n >= 2:
    if n % 2 != 0:
        n -= 1
    for i in range(0, n, 2):
        a[i], a[i + 1] = a[i + 1], a[i]

    print(' '.join(a))
else:
    print(' '.join(a))