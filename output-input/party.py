print('За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.')

a = int(input())
b = int(input())
c = int(input())
a = round((a//2) + (a%2))
b = round((b//2) + (b%2))
c = round((c//2) + (c%2))
print(a + b + c)