# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

s = input()

a = s.find('h')
b = s.rfind('h')
print(s[:a] + s[b:a:-1] + s[b:])