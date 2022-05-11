# Дано два списки чисел. Порахуйте, скільки чисел міститься одночасно як у першому
# списку, так і у другому

a1 = [int(s) for s in input().split()]
a2 = [int(s) for s in input().split()]
print(len(set(a1).intersection(set(a2))))
