# Дано действительное положительное число a и целоe число n.
# Вычислите an. Решение оформите в виде функции power(a, n).
# Стандартной функцией возведения в степень пользоваться нельзя.

def power(a,n):
    res = a
    if n>0:
        for i in range(1, n):
            a = res*a
    elif n<0:
        for i in range(1, abs(n)):
            a = res*a
        a = 1/a
    else:
        a = 1
    return a

a = float(input())
n = int(input())

print(power(a, n))