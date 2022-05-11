# Дано текст: у першому рядку задано число рядків, далі йдуть рядки. Виведіть слово, яке
# найчастіше зустрічається в цьому тексті. Якщо таких слів кілька, виведіть те, що є
# меншим у лексикографічному порядку.

A = {}
B = {}
for i in range(int(input())):
    lst_str = input().split()
    for w in range(len(lst_str)):
        A[lst_str[w]] = A.get(lst_str[w], 0)+1
cnt = sorted(A.items(), key=lambda x: x[1], reverse=True)[0][1]
for key, val in A.items():
    if val == cnt:
        B[key] = cnt
print(sorted(B)[0])
