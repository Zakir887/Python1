# Задача «Количество элементов, которые больше предыдущего»

s, d, i = 0, 0, 0
d = input()
while True:
    s = input()
    if s == '0':
        break
    if int(s) > int(d):
        i += 1
    d = s
print(i)