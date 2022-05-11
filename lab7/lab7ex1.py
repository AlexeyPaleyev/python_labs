# Виведіть номер, під яким Петрик повинен стати в стрій. Якщо в строю є люди з таким
# самим зростом, як у Петрика, то він повинен стати після них

a = [int(s) for s in input().split()]
height = int(input())
res = 1
for i in range(0, len(a)):
    if a[i] >= height:
        res = i + 2
print(res)
