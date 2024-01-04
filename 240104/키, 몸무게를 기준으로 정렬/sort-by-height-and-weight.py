class Student:
    def __init__(self, nm, h, w):
        
        self.n = nm
        self.h = h
        self.w = w
        

n = int(input())

students = []

for i in range(n):

    nm, h, w = tuple(input().split())

    h, w = int(h), int(w)

    students.append(Student(nm,h,w))

students.sort(key=lambda x: (x.h,-x.w)) #

# 정렬 이후 등수별 학생 번호 출력
for student in students :
    print(student.n, student.h, (student.w))