v = int(input())
t = int(input())
s = v * t % 109
if (s < 0):
    print(109 - s)
else:
    print(s)