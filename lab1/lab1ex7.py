# У школі вирішили набрати три нових математичних класи. Лабораторна робота Noз математики у
# них відбуваються одночасно, тому вирішили виділити кабінет для кожного класа і купити в них нові
# парти. За кожною партою може сидіти не більше двох учнів. Відомо кількість учнів у кожному з
# 3
# трьох класів. Скільки всього треба закупити парт, щоб їх хватило на всіх учнів? Програма отримує
# на вхід три натуральних числа: кількість учнів в кажному із трьох класів.

count1 = int(input("Кількість учнів у класі 1 "))
count2 = int(input("Кількість учнів у класі 2 "))
count3 = int(input("Кількість учнів у класі 3 "))
part = count1 // 2 + count1 % 2 + count2 // 2 + count2 % 2 + count3 // 2 + count3 % 2
print("парт потрібно ", part, " шт.")
