'''
# 변수 선언 및 입력
n = int(input())
	
# 좌우 지그재그로 출력합니다.
for i in range(n):
	for j in range(n):
		if i % 2 == 0:
			print((i * n) + j + 1, end=" ")
		else:
			print((i * n) + n - j, end=" ")
	print()
'''

n = int(input())

cnt =0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            cnt += 1
            print(cnt,end=" ")
        cnt += n
    else: 
        for j in range(n):
            
            print(cnt,end=" ")
            cnt -= 1
        cnt += n
    print()