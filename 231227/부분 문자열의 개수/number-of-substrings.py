ch = input()

c = input()

cnt = 0

for i in range(0, len(ch) - len(c) + 2):
    if c == ch[i:(i + len(c))] :
        cnt += 1

print(cnt)