# Равлик повзе по вертикальному жердини висотою h метрів, піднімаючись за день на a
# метрів, а за ніч спускаючись на b метрів. На який день равлик доповзе до вершини
# жердини? Програма отримує на вхід натуральні числа h, a, b. Програма повинна вивести
# одне натуральне число. Гарантується, що a> b

import math
h = int(input("висота "))
a = int(input("за день піднімається "))
b = int(input("за ніч опускається "))
print(math.ceil((h-a) / (a-b)) + 1)
