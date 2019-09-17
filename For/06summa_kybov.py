# Сумма кубов: По данному натуральному n вычислите сумму 13+23+33+...+n3..

n = int(input())
x, s = 0, 0

for s in range(1, n + 1):
    print(s, x)
print(x)