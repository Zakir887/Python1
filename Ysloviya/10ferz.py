print('Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.')

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a - c) == abs(b - d):
    print('YES')
elif a == c or b == d:
    print('YES')
else:
    print('NO')