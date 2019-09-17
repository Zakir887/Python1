print('Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.')

N=int(input())
M=int(input())
x=int(input())
y=int(input())
if N>M:
    N, M = M, N
if x>y:
        x, y = y, x
min = -1
if x==0 or y==0:
    print(0)
else:
    while True:
        min = min+1
        if min==x or min==y or min==N-x or min==M-y or min==N-y or min==M-x:
            print(min)
            break