# Последовательность состоит из различных натуральных чисел и завершается числом 0.
# Определите значение второго по величине элемента в этой последовательности.
# Гарантируется, что в последовательности есть хотя бы два элемента.

x = input()
y = input()
if int(x) > int(y):
    x, y = y, x
while True:
    z = input()
    if z == '0':
        break
    if int(z) > int(y):
        z, y = y, z
    if int(z) > int(x):
        z, x = x, z
print(x)