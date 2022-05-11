# Дано рядок. Видаліть із неї всі символи, чиї індекси діляться на 3.

s = input()
st = ""
for i in range(len(s)):
    if (i) % 3 != 0:
        st += s[i]
print(st)
