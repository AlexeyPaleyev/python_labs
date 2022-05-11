# Як відомо, у США президент обирається не прямим голосуванням, а шляхом дворівневого
# голосування. Спочатку проводяться вибори у кожному штаті та визначається
# переможець виборів у даному штаті. Потім проводяться державні вибори: на цих виборах
# кожен штат має певну кількість голосів — кількість виборців від цього штату. На
# практиці всі виборці від штату голосують відповідно до результатів голосування
# всередині штату, тобто на заключній стадії виборів у голосуванні беруть участь
# штати, що мають різну кількість голосів.
# У першому рядку дано кількість записів. Далі, кожен запис містить прізвище кандидата
# та кількість голосів, відданих за нього в одному зі штатів. Підбіть підсумки виборів: для
# кожного з учасників голосування визначте кількість відданих за нього голосів. Учасників
# слід виводити в алфавітному порядку.

A = {}
B = {}
for i in range(int(input())):
    key, val = input().split()
    if key in A:
        A[key] = A[key] + int(val)
    else:
        A[key] = int(val)
for key in sorted(A):
    print(key, ' ', A[key])
