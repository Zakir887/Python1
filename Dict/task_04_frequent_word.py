# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте
# встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.


d = {}
for i in range(int(input())):
    st = input().split()
    for j in range(len(st)):
        word = st[j]
        d[word] = d.get(word, 0) + 1

max_num = max(d.values())
final_d = {k: v for k, v in d.items() if v == max_num}
print(min(final_d.keys()))