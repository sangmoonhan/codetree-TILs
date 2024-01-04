class point:
    def __init__(self, x1,x2, num):
        
        self.x1 = x1
        self.x2 = x2
        self.n = num
n = int(input())

points = []

for i in range(n):

    x1, x2 = tuple(input().split())

    x1, x2 = int(x1), int(x2)

    points.append(point(x1,x2,(i+1)))

points.sort(key=lambda x: (abs(x.x1) + abs(x.x2) , x.n)) #

# 정렬 이후 등수별 학생 번호 출력
for p in points :
    print(p.n)