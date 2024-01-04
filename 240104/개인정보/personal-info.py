class Student:
    def __init__(self, nm, h, w):
        
        self.n = nm
        self.h = h
        self.w = w
        

n = 5

students = []

for i in range(n):

    nm, h, w = tuple(input().split())

    h, w = int(h), float(w)

    students.append(Student(nm,h,w))

students.sort(key=lambda x: (x.n)) #

# 정렬 이후 등수별 학생 번호 출력
print("name")
for student in students :
    print(student.n, student.h, "{:.1f}".format(student.w))

print()

students.sort(key=lambda x: (-x.h)) #

print("height")
for student in students :
    print(student.n, student.h, "{:.1f}".format(student.w))