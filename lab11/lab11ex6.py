# Даний текст: у першому рядку записано кількість рядків у тексті, а потім самі рядки.
# Виведіть усі слова, що зустрічаються в тексті, по одному на кожен рядок. Слова повинні
# бути відсортовані за спаданням їхньої кількості появи в тексті, а при однаковій частоті
# появи — у лексикографічному порядку.
# Вказівка. Після того, як ви створите словник всіх слів, вам захочеться відсортувати його
# за частотою слова. Бажаного можна домогтися, якщо створити список, елементами
# якого будуть кортежі з двох елементів: частота слова і саме слово. Наприклад, [(2, 'hi'),
# (1, 'what'), (3, 'is')]. Тоді стандартне сортування сортуватиме список кортежів, при цьому
# кортежі порівнюються по першому елементу, а якщо вони рівні - то по другому. Це майже
# те, що потрібно в завданні.

def sorting(n):
    return -n[0], n[1]


d = {}
lst = []
lsts = []
for nn in range(int(input())):
    for w in input().split():
        d[w] = d.get(w, 0) + 1
for w, c in d.items():
    lst.append((c, w))
lsts = sorted(lst, key=sorting)
for i in range(len(lsts)):
    print(lsts[i][1])