print('Даны три целых числа. Выведите значение наименьшего из них.')

a = int(input())
b = int(input())
c = int(input())
if a < b:
  b = a
if b < c:
  c = b
print(c)