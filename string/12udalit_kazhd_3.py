# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

s = input()
n = ''
for x in range(len(s)):
    if x % 3 != 0:
        n += s[x]
print(n)
