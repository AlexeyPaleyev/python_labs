# Дано два числа n і m. Створіть двовимірний масив розміром n×m та заповніть його
# символами "." та "*" у шаховому порядку. У лівому верхньому кутку має стояти крапка

n, m = [int(s) for s in input().split()]
if m % 2 == 0:
    a = [([".","*"]) * (m/2) for i in range(n)]
    for j in range(1, n, 2):
        a[j] = ["*","."] * (m // 2)

else:
    a = [(([".","*"]) * (m // 2) + ["."]) for i in range(n)]
    for j in range(1, n, 2):
        a[j] = ["*","."] * (m // 2) + ["*"]
for row in a:
    print(' '.join([str(el) for el in row]))
