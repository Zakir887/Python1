# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же,
# как у Пети, то он должен встать после них.

a = [int(i) for i in input().split()]
x = int(input())

d = int(len(a))
if x > a[d - 1]:
    for i in range(0, len(a)):
        if x > a[i]:
            break
    print(i + 1)
else:
    print(d + 1)
