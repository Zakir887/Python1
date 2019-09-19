# Пример реализации алгоритма сортировки Insertion Sort

print('Пример реализации алгоритма сортировки Insertion Sort на случайном списке:')
from random import randrange
n = 50
i, j, d  = 0, 0, 0
a = [randrange(1, 100) for i in range(n)]
print(' '.join([str(i) for i in a]), '\n')

# Этот алгоритм сегментирует список на две части: отсортированную и неотсортированную. Алгоритм перебирает второй
# сегмент и вставляет текущий элемент в правильную позицию первого сегмента.
print('Insertion Sort:')

for i in range(1,len(a)):
    d = a[i]
    j = i - 1
    while j >= 0 and a[j] > d:
        a[j + 1] = a[j]
        a[j] = d
        j -= 1
print(' '.join([str(i) for i in a]), '\n')