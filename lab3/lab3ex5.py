# В деякій школі Лабораторна робота №починаються о 9:00. Тривалість уроку - 45 хвилин,
# після 1-го, 3-го, 5-го і т.д. уроків перерва 5 хвилин, а після 2-го, 4-го, 6-го і т.д. - 15 хвилин.
# Дано номер уроку (число від 1 до 10). Визначте, коли закінчується зазначений урок.
# Виведіть два цілих числа: час закінчення уроку в годинах і хвилинах

n = int(input("номер уроку (число від 1 до 10) "))
t = n * 45
t = t + ((n - 1) // 2) * 15
t = t + ((n) // 2) * 5
print(9 + t // 60, t % 60)