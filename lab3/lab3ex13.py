# З початку доби минуло H годин, M хвилин, S секунд (0 ≤ H <12, 0 ≤ M <60, 0 ≤ S <60). За
# даними числах H, M, S визначте кут (в градусах), на який повернулаcь годинникова стрілка
# з початку доби і виведіть його у вигляді дійсного числа

h = int(input("годин "))
m = int(input("хвилин "))
s = int(input("секунд "))
res = 360/12 * h + 360/(12*60)*m + 360/(12*3600)*s
print(res)
