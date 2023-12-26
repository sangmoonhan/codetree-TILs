arr = ["apple", "banana", "grape", "blueberry", "orange"]

ch = input()

cnt = 0

for i in arr:
    if i[2] == ch or i[3] == ch :
        print(i)
        cnt += 1

print(cnt)