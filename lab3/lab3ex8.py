# Дано значення двох моментів часу, що належать одній і тій же добі: години, хвилини і
# секунди для кожного з моментів часу. Відомо, що другий момент часу настав не раніше
# першого. Визначте, скільки секунд пройшло між двома моментами часу.
# Програма на вхід отримує три цілих числа: години, хвилини, секунди, що задають перший
# момент часу і три цілих числа, які задають другий момент часу.
# Виведіть число секунд між цими моментами часу

h1 = int(input("години1 "))
m1 = int(input("хвилини1 "))
s1 = int(input("секунди1 "))
h2 = int(input("години2 "))
m2 = int(input("хвилини2 "))
s2 = int(input("секунди2 "))
print((h2 - h1) * 60 * 60 + (m2 - m1) * 60 + (s2 - s1))