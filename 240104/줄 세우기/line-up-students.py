class Student:
    def __init__(self, h,w,num):
        self.h = h
        self.w = w
        self.n = num

n = int(input())

students = []

for i in range(n):

    h, w = tuple(map(int,input().split()))

    students.append(Student(h,w,(i+1)))

students.sort(key=lambda x: (-x.h, -x.w, x.n)) # 국어 점수 기준 내림차순 정렬

# 정렬 이후 등수별 학생 번호 출력
for student in students :
    print(student.h, student.w, student.n)