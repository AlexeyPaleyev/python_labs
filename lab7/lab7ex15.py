# N кеглів виставили в один ряд, пронумерувавши їх зліва направо числами від 1 до N. Потім
# по цьому ряду кинули K куль, при цьому i-а куля збила всі кеглі з номерами від li до ri
# включно. Визначте які кеглі залишилися стояти на місці.
# Програма отримує на вхід кількість кеглів N та кількість кидків K. Далі йде K пар чисел li,
# ri, при цьому 1≤li≤ri≤N.
# Програма повинна вивести послідовність із N символів, де j-й символ є “I”, якщо j-я кегля
# залишилася стояти, або “.”, якщо j-я кегля була збита.

n, k = [int(s) for s in input().split()]
n_list = [i for i in range(1, n + 1)]
for i in range(k):
    start, end = [int(s) for s in input().split()]
    for j in range(start, end + 1):
        n_list[j-1] = 0
res = ""
for i in range(n):
    if n_list[i] == 0:
        res += "."
    else:
        res += "I"
print(res)
