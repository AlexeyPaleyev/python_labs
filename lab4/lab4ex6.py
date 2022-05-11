# По даному натуральному числу n обчисліть суму кубів: 13+23+33+...+n3.

n = int(input())
res = 0
for i in range(1, n+1):
    res += i**3
print(res)
