ch = input()
print(ch)
n = len(ch)

for _ in range(n):
    ch = ch[-1] + ch[:-1]
    print(ch)