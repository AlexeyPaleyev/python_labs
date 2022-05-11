# У генеалогічному дереві визначте для двох елементів найменшого загального предка
# (Lowest Common Ancestor). Найменшим загальним предком елементів A і B є такий
# елемент C, що є предком A, C є предком B, при цьому глибина C є найбільшою з можливих.
# При цьому елемент вважається своїм предком.
# Формат вхідних даних аналогічний до попереднього завдання
# Для кожного запиту виведіть найменшого загального предка цих елементів.

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
for i in range(len(T)):
    for k, v in T.items():
        v = v.insert(0, k)


for k in range(int(input())):
    f, s = input().split(' ')
    for parent in T[f]:
        if parent in T[s]:
            print(parent)
            break
