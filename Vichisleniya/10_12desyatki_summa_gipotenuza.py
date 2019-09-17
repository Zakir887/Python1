print('Дано натуральное число. Найдите число десятков в его десятичной записи.')

x = str(input())
if len(x) < 2:
    print(0)
else:
    print(str(x[-2]))

print('Дано трехзначное число. Найдите сумму его цифр.')
y = str(input())
c = 0
b = int(len(y))
d = int(0)
for c in range(0, b):
	d = int(y[c]) +d
print(d)

print('Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.')
a = int(input())
b = int(input())
c = 0

print((a**2 + b**2)**0.5)