# Политическая жизнь одной страны очень оживленная. В стране действует K политических партий, каждая из которых
# регулярно объявляет национальную забастовку. Дни, когда хотя бы одна из партий объявляет забастовку, при условии,
# что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.
#
# i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i. То есть i-я партия объявляет
# забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д. Если в какой-то день несколько партий объявляет забастовку,
# то это считается одной общенациональной забастовкой.
#
# В календаре страны N дней, пронумерованных, начиная с единицы. Первый день года является понедельником, шестой и
# седьмой дни года — выходные, неделя состоит из семи дней.
#
# В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок. i-я строка содержит
# числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.


N, k = [int(i) for i in input().split()]
year = set()
strike = set()
res = set()
for i in range(1, N + 1):
    if i % 6 != 0 and i % 7 != 0:
        year.add(i)

for i in range(k):
    a_i, b_i = [int(i) for i in input().split()]
    for j in range(a_i, N + 1, b_i):
        if j % 6 != 0 and j % 7 != 0:
            strike.add(j)

res = year & strike
print(len(res))