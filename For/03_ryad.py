# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой
# задаче можно обойтись без инструкции if.

a = int(input())
b = int(input())
s = 0
p = 0
for s in range(a, b - 1, -1):
    if s % 2 != 0:
        print(s)