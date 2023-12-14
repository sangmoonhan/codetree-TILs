p1 = input().split()
p2 = input().split()
p3 = input().split()

g1 = p1[0]
g2 = p2[0]
g3 = p3[0]

c1 = int(p1[1])
c2 = int(p2[1])
c3 = int(p3[1])

if g1 == "Y" and c1 >= 37 :
    if g2 == "Y" and c2 >= 37 :
        print("E")
    elif g3 == "Y" and c3 >= 37 :
        print("E")
    else : print("N")
else : 
    if g2 == "Y" and c2 >= 37 :
        if g3 == "Y" and c3 >= 37:
            print("E")
        else :
            print("N")
    else :
        print("N")

# 변수 선언 및 입력
#inp = input().split()
#c1, t1 = inp[0], int(inp[1])
#inp = input().split()
#c2, t2 = inp[0], int(inp[1])
#inp = input().split()
#c3, t3 = inp[0], int(inp[1])

# A가 2명 이상인지 판단하기
#if c1 == 'Y' and t1 >= 37:
#    # 첫 번째 사람이 A라면, 남은 두 사람 중 한 사람이라도 A면 됩니다.
#    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
#        print("E")
#    else:
#        print("N")
#else:
#    # 첫 번째 사람이 A가 아니라면, 남은 두 사람 모두 A여야만 합니다.
#    if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
#        print("E")
#    else:
#        print("N")