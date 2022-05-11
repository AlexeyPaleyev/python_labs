# Дано три цілих числа. Визначте найменше з них

first = int(input("Число 1 "))
second = int(input("Число 2 "))
three = int(input("Число 3 "))
res = three
if first <= second and first <= three:
    res = first
elif second <= first and second <= three:
    res = second
print(res)
