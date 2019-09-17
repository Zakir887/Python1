h = int(input())
a = int(input())
b = int(input())
D = 0
while True:
    D= D+1
    h = h - a
    if h <= 0:
        break
    h = h + b
print(D)