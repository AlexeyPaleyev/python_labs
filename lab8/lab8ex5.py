# Дана послідовність цілих чисел, що закінчується числом 0. Виведіть цю послідовність у
# зворотному порядку.
# При вирішенні цього завдання не можна користуватися масивами та іншими
# динамічними структурами даних. Рекурсія допоможе.

def rec():
    n = int(input())
    if n != 0:
        rec()
        print(n)


print(0)
rec()
