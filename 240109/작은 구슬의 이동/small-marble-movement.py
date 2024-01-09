n, t = tuple(map(int,input().split()))

x, y, d = tuple(input().split())

x, y = int(x)-1, int(y)-1

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

while t:
    if in_range(x + dxs[move_dir], y + dys[move_dir]) : 

        x, y = x + dxs[move_dir], y + dys[move_dir]
        t -= 1
    
    else:  # check whether position is out of grid
        
        move_dir = 3 - move_dir # change direction
        t -= 1
    
print(x+1,y+1)