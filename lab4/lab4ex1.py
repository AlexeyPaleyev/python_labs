#Дано два цілих числа A і B (при цьому A ≤ B). Виведіть всі числа від A до B включно

a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)