n = int(input())

curr = [0] * 200001
black = [0] * 200001
white = [0] * 200001
w,b,g = 0,0,0

start = 100000
for j in range(n):

    cnt, direction = input().split()
    cnt = int(cnt)

    if direction == "R":
        for i in range(start,start+cnt):
            curr[i] = 1
            black[i] += 1 
        start += (cnt-1)
    elif direction == "L":
        for i in range(start-cnt+1, start+1):
            curr[i] = 2
            white[i] += 1
        start -= (cnt-1)
    
for i in range(200001):
    if curr[i] == 1:
        b += 1
    elif curr[i] == 2:
        w += 1

print(w,b)