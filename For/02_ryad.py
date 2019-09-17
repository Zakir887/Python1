# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

a = int(input())
b = int(input())
s = 0
p = 0
if a < b:
    s = 0
    for s in range(a, b + 1):
        print(s)
else:
    for s in range(a, b - 1, -1):
        print(s)
