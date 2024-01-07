input_list = [list(map(int,input().split())) for _ in range(2)]

offset = 1000
max_number = 2001

area_list = [[0] * max_number for _ in range(max_number)]

x1, y1, x2, y2 = input_list[0]

for idx in range(x1+offset, x2+offset+1):
    for idy in range(y1+offset, y2+offset+1):
        area_list[idx][idy] = 1 

x1, y1, x2, y2 = input_list[1]

for idx in range(x1+offset, x2+offset+1):
    for idy in range(y1+offset, y2+offset+1):
        area_list[idx][idy] = 0  

empty_list = list()

# 겹치지 않는 영역들의 위치 정보를 empty_list에 저장합니다.

for dx in range(2001):
    for dy in range(2001):
        if area_list[dx][dy] == 1:
            empty_list.append([dx,dy])

min_x, min_y = 2001,2001
max_x, max_y = 0,0

if empty_list == []:
    print(0)
else:
    
    for value in empty_list:
        min_x ,max_x = min(min_x,value[0]), max(max_x, value[0])
        min_y, max_y = min(min_y,value[1]), max(max_y,value[1])
    
    answer = (max_x - min_x) * (max_y - min_y)
    
    print(answer)