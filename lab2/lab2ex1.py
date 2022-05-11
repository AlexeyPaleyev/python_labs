# Дано два цілих числа. Виведіть значення найменшого з них

num1 = int(input("Число 1 "))
num2 = int(input("Число 2 "))
if num1 < num2:
    print("Найменше ", num1 )
elif num1 > num2:
    print("Найменше ", num2 )
else:
    print("Числа рівні ")

