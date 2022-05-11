# Дано список країн та міст кожної країни. Потім дано назви міст. Для кожного міста
# вкажіть, в якій країні воно знаходиться.

d = {}
s = []
for i in range(int(input())):
    s = input().split()
    k = s[0]
    s.pop(0)
    d[k] = s
for i in range(int(input())):
    q = input()
    for k, v in d.items():
        if q in v:
            print(k)
