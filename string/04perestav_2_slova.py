# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в
# строку и выведите получившуюся строку.
# При решении этой задачи не стоит пользоваться циклами и инструкцией if.

s = input()
x = int(s.find(' '))
print(s[x+1:], s[:x])
