# Дано два списки чисел. Знайдіть усі числа, які входять як до першого, так і до другого
# списку і виведіть їх у порядку зростання

a1 = [int(s) for s in input().split()]
a2 = [int(s) for s in input().split()]
print(" ".join(str(s) for s in sorted(list(set(a1).intersection(set(a2))))))
