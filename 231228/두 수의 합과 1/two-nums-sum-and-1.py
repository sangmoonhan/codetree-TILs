n = str(sum(list(map(int,input().split()))))

cnt = 0

for i in n :
    if i == '1' :
        cnt += 1

print(cnt)