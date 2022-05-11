# Дано список. Виведіть ті його елементи, які зустрічаються у списку лише один раз.
# Елементи потрібно виводити у порядку, у якому зустрічаються у списку.

a = [int(s) for s in input().split()]
res = []
for i in range(len(a)):
    s = str(a[i])
    for j in range(len(a)):
        # print(a[i], a[j])
        if a[j] == a[i] and i != j:
            s = ""

            break

    res.append(s)
print(" ".join(res))
