# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой
# стране он находится.

D = {}
for i in range(int(input())):
    country = input().split()
    x = country[0]
    for j in range(len(country)-1):
        y = country[j+1]
        D[y] = x

for i in range(int(input())):
    print(D[input()])