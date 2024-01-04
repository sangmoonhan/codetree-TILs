n = int(input())

class Student:
    def __init__(self, nm, kor, eng, math):
        self.nm = nm
        self.kor = kor
        self.eng = eng
        self.math = math

students = []

for i in range(n):

    nm, k, e, m = input().split()

    k, e, m = int(k), int(e), int(m)

    students.append(Student(nm,k,e,m))



# 점수의 총합 기준 오름차순
students.sort(key=lambda x: (x.kor + x.eng + x.math)) 

for student in students: # 정렬 이후의 결과 출력
    print(student.nm, student.kor, student.eng, student.math)