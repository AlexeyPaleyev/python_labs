# Довжина кільцевої автомобільної дороги - 109 кілометрів. Байкер Вася стартує з
# нульового кілометра і їде зі швидкістю v кілометрів на годину. На якій позначці він
# зупиниться через t годин? Програма отримує на вхід значення v і t. Якщо v>0, то Вася
# рухається в додатному напрямку, якщо ж значення v<0, то в від’ємному. Програма
# повинна вивести ціле число від 0 до 108 - номер позначки, на якій зупиниться Вася

v = int(input("Швидкість "))
t = int(input("Час "))
if v > 0:
    print(v * t % 109)
else:
    if v * t % 109 == 0:
        print(0)
    else:
        print(109 - ((-v * t) % 109))
