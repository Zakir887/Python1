# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том
# порядке, в котором они встречаются в списке.


a = [i for i in input().split()]

n = len(a)
y = 0
for i in range(n):
    y = 0
    for j in range(n):
        if a[i] == a[j]:
            y += 1
    if y == 1:
        print(a[i])