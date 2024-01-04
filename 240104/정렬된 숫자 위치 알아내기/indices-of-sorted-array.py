class point:
    def __init__(self, n, idx):
        
        self.n = n
        self.idx = idx

n = int(input())

arr = list(map(int,input().split()))

brr = []

for i in range(n):

    k = arr[i]

    brr.append(point(k,(i+1)))

brr.sort(key=lambda x: x.n) #



# 정렬 이후 등수별 학생 번호 출력
for j in range(1,n+1):
    for i ,p in enumerate(brr,start=1) :

        if p.idx == j :
            print(i, end=" ")
            break