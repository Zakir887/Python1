# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input())
c, f, s = 0, 1, 0

for c in range(1, n+1):
    f *= c
    s += f
print(s)