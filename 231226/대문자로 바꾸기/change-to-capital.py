# 2차원 배열을 구현해 각 줄마다 알파벳 소문자를 입력받습니다.
arr_2d = [
	list(input().split())
	for _ in range(5)
]

# 알파벳 소문자를 대문자로 바꾸어 출력합니다.
for i in range(5):
	for j in range(3):
		arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
		print(arr_2d[i][j], end=" ")
	print()

#for i in range(5):
#    arr = input().split()
#
#    for j in range(3):
#        print(arr[j].upper(), end=" ")
#    print()