# Дано двовимірний масив і два числа: i та j. Поміняйте у масиві стовпці з номерами i та j
# та виведіть результат. Програма отримує на вхід розміри масиву n та m, потім
# елементи масиву, потім числа i та j. Рішення оформіть як функції swap_columns(a, i, j)

n, m = [int(s) for s in input().split()]
arr = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(s) for s in input().split()]


def swap_columns(a, r, c):
    for k in range(n):
        a[k][r], a[k][c] = a[k][c], a[k][r]
    return a


for row in swap_columns(arr, i, j):
    print(' '.join(str(el) for el in row))
