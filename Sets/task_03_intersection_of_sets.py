# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

print(*sorted(set(input().split()) & (set(input().split())), key=int))