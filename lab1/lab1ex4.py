# Дано число n. З початку доби пройшло n хвилин. Визначте, скільки годин і хвилин буде показувати
# електронний годинник у цей момент. Програма повинна вивести два числа: кількість годин (від 0
# до 23) і кількість хвилин (від 0 до 59). Урахуйте, що число n може бути більше, чим кількість хвилин
# у добі.

n = int(input("Кількість хвилин "))

print("Час ", (n // 60) % 24,  ":", n % 60)
