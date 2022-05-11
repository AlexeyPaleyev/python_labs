# Дано список чисел. Виведіть всі елементи списку, які більші за попередній елемент.

s = input()
a = [int(s) for s in s.split()]

for i in range(1, len(a)):
    if a[i-1] < a[i]:
        print(a[i])
