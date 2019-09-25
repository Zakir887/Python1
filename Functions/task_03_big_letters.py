# Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую
# букву на большую.
# Например, print(capitalize('word')) должно печатать слово Word.
#
# На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв.
# Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу
# функцию capitalize().

def capitolize(a):
    for i in range(len(a)):
        x = a[i]
        k = ord(x[0]) - 32
        b = chr(k)
        a[i] = x.replace(x[0], b, 1)
    return a


a = [str(s) for s in input().split()]
b = capitolize(a)

print(' '.join(b))