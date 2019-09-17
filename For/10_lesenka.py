# По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())
x, s , m = 0, 0, 1

for s in range (1, n+1):
    m = 0
    for x in range(0, s):
        m += 1
        print(m, sep='', end='')
    print()
