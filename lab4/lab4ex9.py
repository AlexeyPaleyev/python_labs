# Дано N чисел: спочатку вводиться число N, потім вводиться рівно N цілих чисел. Підрахуйте
# кількість нулів серед введених чисел та виведіть цю кількість. Вам потрібно підрахувати
# кількість чисел, рівних нулю, а не кількість цифр

n = int(input())
res = 0
for i in range(n):
    if int(input()) == 0:
        res += 1
print(res)
