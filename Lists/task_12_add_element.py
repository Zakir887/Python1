# Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C,
# сдвинув все элементы, имевшие индекс не менее k, вправо.
# Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет
# добавить новый элемент, используя метод append.
#
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая
# дополнительного списка.

a = [i for i in input().split()]
x = [i for i in input().split()]
a.append(0)

i = len(a) - 1
j = int(x[0])

while i > j:
    a[i], a[i - 1] = a[i - 1], a[i]
    i -= 1

c = int(x[0])
a[c] = x[1]
print(' '.join([str(i) for i in a]))