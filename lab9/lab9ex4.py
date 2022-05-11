# Дано число n. Створіть масив розміром n×n та заповніть його за наступним правилом.
# На головній діагоналі мають бути записані числа 0. На двох діагоналях, що прилягають
# до головної, числа 1. На наступних двох діагоналях числа 2 тощо

n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)

for row in a:
    print(" ".join(str(el) for el in row))