# У списку всі елементи є різними. Поміняйте місцями мінімальний та максимальний
# елемент цього списку.

a = [int(s) for s in input().split()]
mi, ma = a[0], a[0]
i_mi, i_ma = 0, 0
for i in range(1, len(a)):
    if mi > a[i]:
        mi, i_mi = a[i], i
    elif ma < a[i]:
        ma, i_ma = a[i], i
a[i_mi], a[i_ma] = a[i_ma], a[i_mi]
print(' '.join(str(s) for s in a))
