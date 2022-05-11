# Відомо, що на дошці 8×8 можна розставити 8 ферзів так, щоб вони не били один одного.
# Вам дано розміщення 8 ферзів на дошці, визначте, чи є серед них пара, що б'ють один
# одного. Програма отримує на вхід вісім пар чисел, кожне число від 1 до 8 – координати 8
# ферзів. Якщо ферзі не б'ють один одного, виведіть слово NO, інакше виведіть YES

lst_x = []
lst_y = []
for i in range(8):
    x, y = [int(s) for s in input().split()]
    lst_x.append(x)
    lst_y. append(y)
res = "NO"
for i in range(8):
    for j in range(i + 1, 8):
        if lst_x[i] == lst_x[j] or lst_y[i] == lst_y[j] or abs(lst_x[i] - lst_x[j]) == abs(lst_y[i] - lst_y[j]):
            res = "YES"
print(res)
