class Agent:
    def __init__(self, n, k, e, m):
        self.n = n
        self.k = k
        self.e = e
        self.m = m

n = int(input())

agents = []
for _ in range(n):
    n, k ,e ,m = tuple(input().split())
    
    k ,e ,m = int(k), int(e), int(m)

    agents.append(Agent(n, k ,e ,m))

agents.sort(key=lambda x : (-x.k, -x.e, -x.m))


for i in agents :
    
    print(i.n , i.k, i.e, i.m)