# Переставте сусідні елементи списку (A[0] з A[1], A[2] з A[3] тощо). Якщо елементів
# непарна кількість, то останній елемент залишається на своєму місці.

a = [int(s) for s in input().split()]
for i in range(0, len(a)-1, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(' '.join(str(s) for s in a))
