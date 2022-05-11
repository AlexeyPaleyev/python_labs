# Ваня та Марійка грають у гру. Ваня загадав натуральне число від 1 до n. Марійка
# намагається вгадати це число, для цього вона називає деякі множини натуральних чисел.
# Ваня відповідає Марійці YES, якщо серед названих їй чисел є задумане, інакше - NO. Після
# кількох заданих питань Марійка заплуталася в тому, які питання вона ставила і які
# відповіді отримала і просить вас допомогти їй визначити, які числа міг задумати Ваня.18
# У першому рядку задано n – максимальне число, яке міг загадати Ваня. Далі кожен рядок
# містить питання Марійки (множину чисел, розділених пробілом) і відповідь Вані на це
# питання.
# Ви повинні вивести через пробіл у порядку зростання всі числа, які міг задумати Ваня

n = int(input())
A = set([i for i in range(n)])
while True:
    word = input()
    if word == "YES":
        A.intersection_update(set(a))
    elif word == "NO":
        A.difference_update(set(a))
    elif word == "HELP":
        break
    else:
        a = [int(s) for s in word.split()]

print(" ".join(str(s) for s in sorted(A)))
