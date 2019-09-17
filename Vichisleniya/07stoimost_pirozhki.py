from math import ceil

a = int(input())#рубли
b = int(input())#копейки
n = int(input())#кол-во пирожков
x = n*(a*100 + b)
print(int(x//100), (x%100))