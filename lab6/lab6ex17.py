# Дано послідовність натуральних чисел x1, x2, ..., xn.
# Визначте стандартне відхилення для цієї послідовності натуральних чисел, що
# завершується числом 0.

x = int(input())
n = sm = sumsq = 0
while x != 0:
    n += 1
    sm += x
    sumsq += x**2
    x = int(input())
print(((sumsq - sm**2/n)/(n-1))**0.5)
