# Послідовність складається з натуральних чисел і завершується числом 0. Визначте,
# скільки елементів цієї послідовності більше за попередній елемент.

k = 0
n = int(input())
more = n
while n != 0:
    if n > more:
        k += 1
    more = n
    n = int(input())
print(k)