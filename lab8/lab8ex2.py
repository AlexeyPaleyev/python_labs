# Дано дійсне позитивне число a і ціле число n. Обчисліть an. Рішення оформіть як функції
# power(a, n). Стандартною функцією зведення в степінь користуватися не можна.


def power(d, st):
    res = 1
    for i in range(abs(st)):
        res = res * d
    if n < 0:
        res = 1 / res
    return (res)


a = float(input())
n = int(input())
print(power(a, n))
