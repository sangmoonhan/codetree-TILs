def print_star(n):    # 1부터 n번째 줄까지 별을 출력하는 함수
    if n == 0:        # 종료 조건
        return

    print_star(n - 1) # 1부터 n - 1번째 줄까지 출력하는 함수
    print("*" * n)    # n번째 줄에는 n개의 별을 출력합니다.

n = int(input())

print_star(n)