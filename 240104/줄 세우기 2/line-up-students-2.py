class Student:
    def __init__(self, h, w, idx):
        
        self.h = h
        self.w = w
        self.idx = idx

n = int(input())

brr = []

for i in range(n):

    h, w = tuple(map(int,input().split()))

    brr.append(Student(h,w,(i+1)))

brr.sort(key=lambda x: (x.h,-x.w)) #

for st in brr :
    print(st.h, st.w, st.idx)