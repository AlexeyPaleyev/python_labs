# Послідовність складається із натуральних чисел і завершується числом 0. Визначте
# значення найбільшого елемента послідовності.

m = 0
n = int(input())
while n != 0:
    if n > m:
        m = n
    n = int(input())
print(m)
