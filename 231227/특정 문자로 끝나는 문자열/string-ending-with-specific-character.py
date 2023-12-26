arr = []


for i in range(10) :
    arr.append(input())

ch = input()

cnt = 0

for i in arr :
    if ch == i[-1]:
        print(i)
        cnt += 1

if cnt == 0 :
    print("None")