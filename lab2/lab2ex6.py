# Дано три цілих числа. Визначте, скільки серед них збігаються. Програма повинна вивести
# одне з чисел: 3 (якщо всі збігаються), 2 (якщо два збігається) або 0 (якщо все числа різні).

first = int(input("Число 1 "))
second = int(input("Число 2 "))
three = int(input("Число 3 "))
res = 2
if first == second == three:
    res = 3
elif first != second and first != three and second != three:
    res = 0
print(res)
