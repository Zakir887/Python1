# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.


a = [i for i in input().split()]

n = len(a)
y = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            y += 1
print(y)