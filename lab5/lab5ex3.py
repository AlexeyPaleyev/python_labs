# Дано рядок. Розріжте її на дві рівні частини (якщо довжина рядка – парна, а якщо довжина
# рядка непарна, то довжина першої частини має бути на один символ більша).
# Переставте ці дві частини місцями, результат запишіть у новий рядок та виведіть на
# екран. При вирішенні цього завдання не варто користуватися інструкцією if.

import math
s = input()
m = math.ceil(len(s)/2)
print(s[m:] + s[:m])