# За натуральним числом n ≤ 9 виведіть драбинку з n сходинок, i-я сходинка складається з чисел від
# 1 до i без пробілів.

n = int(input()) + 1
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end="")
    print("")
