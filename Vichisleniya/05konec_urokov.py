u = int(input())
x = 540
y = u
for u in range(0, u):
    if u%2==0:
        x += 60
    else:
        x += 50
if y%2==0:
    x -= 15
else:
    x -= 15
print(x//60, x%60)