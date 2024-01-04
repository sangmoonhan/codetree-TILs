class Agent:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

n = int(input())

agents = []
for _ in range(n):
    n, h, w = tuple(input().split())
    
    agents.append(Agent(n, h, w))

agents.sort(key=lambda x : x.h)


for i in agents :
    
    print(i.n , i.h, i.w)