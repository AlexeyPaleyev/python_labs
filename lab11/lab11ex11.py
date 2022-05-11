# Дано два елементи в дереві. Визначте, чи є один із них нащадком іншого.
# У вхідних даних записано дерево в тому ж форматі, що і в попередній задачі. Далі йде
# число запитів K. У кожному з наступних рядків K, містяться імена двох елементів дерева.
# Для кожного такого запиту виведіть одне з трьох чисел: 1, якщо перший елемент є
# предком другого, 2 якщо другий є предком першого або 0, якщо жоден з них не є предком
# іншого.

T = {}
k = []
for n in range(int(input())-1):
    k = input().split(' ')
    T[k[0]] = [k[1]]
for i in range(len(T)):
    for k, v in T.items():
        if v[-1] in T.keys():
            T[k] = T[k] + (T[v[-1]])
T[(list(T.values())[0][-1])] = []
for k in range(int(input())):
    f, s = input().split(' ')
    if f in T[s]:
        print(1)
    elif s in T[f]:
        print(2)
    else:
        print(0)
