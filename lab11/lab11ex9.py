# Дана база даних про продаж деякого інтернет-магазину. Кожен рядок вхідного файлу
# являє собою запис виду Покупець товар кількість, де Покупець - ім'я покупця (рядок без
# прогалин), товар - назва товару (рядок без прогалин), кількість - кількість придбаних
# одиниць товару.
# Створіть перелік всіх покупців, а кожного покупця підрахуйте кількість придбаних ним
# одиниць кожного виду товарів. Список покупців, а також список товарів для кожного
# покупця слід виводити у лексикографічному порядку.

from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)

for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])
