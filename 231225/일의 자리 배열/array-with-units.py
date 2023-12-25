arr = list(map(int,input().split()))

brr = [arr[0], arr[1]]

# 3번째 항부터 10번째 항까지 추가
for i in range(8): 
    brr.append( (brr[-1] + brr[-2]) % 10 )

for i in brr:
    print(i, end=" ")