# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести
# количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0,
# считывать не нужно.

i, s = 0, 0

while True:
    i += 1
    s = input()
    if s == '0':
        break
print(i-1)