# З початку доби годинникова стрілка повернулася на кут в α градусів. Визначте на який
# кут повернулась хвилинна стрілка з початку останньої години. Вхідні і вихідні дані - дійсні
# числа.

a = float(input("градусів "))
print((a * 12) % 360)