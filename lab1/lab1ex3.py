# n школярів ділять k яблук порівну, остача залишається в кошику. Скільки яблук отримає
# кожен школяр? Скільки яблук залишиться у кошику? Програма отримує на вхід числа n і k
# та повинна вивести кількості яблук (два числа).

n = int(input("Кількість школярів "))
k = int(input("Кількість яблук "))

print("Кожен школяр отримає ", k//n, " яблук(а)")

print("У кошику залишиться ", k % n, " яблук(а)")
