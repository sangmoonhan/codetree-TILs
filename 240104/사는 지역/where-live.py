class Agent:
    def __init__(self, nm, bj, lc):
        self.nm = nm
        self.bj = bj
        self.lc = lc

n = int(input())

agents = []
for _ in range(n):
    nm, bj, lc = tuple(input().split())
    
    agents.append(Agent(nm, bj,lc))

min_a = agents[0]

for i in range(1,n):

    if min_a.nm < agents[i].nm:

        min_a = agents[i]

print("name", min_a.nm)
print("addr", min_a.bj)
print("city", min_a.lc)