word = ['L', 'E', 'B', 'R', 'O', 'S']

n = input()

# 해당 문자를 찾지 못했다면 -1
idx = -1

if n in word :
    print(word.index(n))