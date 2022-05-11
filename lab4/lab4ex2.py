# Дано два цілих числа A і В. Виведіть всі числа від A до B включно у порядку зростання, якщо A < B,
# або в порядку спадання в протилежному випадку.

a = int(input())
b = int(input())
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b - 1, - 1):
        print(i)
