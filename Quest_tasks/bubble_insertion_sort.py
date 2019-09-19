# Примеры реализации алгоритмов сортировки Bubble Sort и Insertion Sort

print('Примеры реализации алгоритмов сортировки Bubble Sort и Insertion Sort на случайном списке:')
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


# Этот алгоритм сегментирует список на две части: отсортированную и неотсортированную. Алгоритм перебирает второй
# сегмент и вставляет текущий элемент в правильную позицию первого сегмента.
print('Insertion Sort:')
while i < n - 1:
    i = n[i]
    j = i - 1
    while j >= 0 and n[j] > i:
        n[j + 1] = n[j]
        j -= 1
    n[j + 1] = i
print(' '.join([str(i) for i in a]), '\n')
