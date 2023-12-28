ch = input()

idx = ch.index('e')

ch = list(ch)

ch.pop(idx)

ch = ''.join(ch)

print(ch)