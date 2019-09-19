# Пример реализации алгоритма сортировки Bubble Sort

print('Пример реализации алгоритма сортировки Bubble Sort на случайном списке:')
from random import randrange
n = 50
a = [randrange(1, 100) for i in range(n)]
print(' '.join([str(i) for i in a]), '\n')


# После первого прохода по массиву самое большое число окажется в конце, а когда первый элемент будет не с чем
# сравнить, массив будет отсортирован по возрастанию.
print('Bubble Sort:')
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1
print(' '.join([str(i) for i in a]), '\n')