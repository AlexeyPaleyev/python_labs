# За цим натуральним n обчисліть суму 1!+2!+3!+...+n!. У розв’язанні цієї задачі можна
# використовувати лише один цикл. Користуватися математичною бібліотекою math у цій задачі
# заборонено.

n = int(input())
f = 1
res = 0
for i in range(1, n+1):
    f *= i
    res += f
print(res)
