# Визначте суму всіх елементів послідовності, що завершується числом 0. У цій та у всіх
# наступних задачах числа, що йдуть за першим нулем, враховувати не потрібно.

s = 0
while True:
    i = int(input())
    if  i !=0:
        s += i
    else:
        break
print(s)
