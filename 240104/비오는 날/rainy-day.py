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

min_a = Agent("2111-08-19", "Thu", "Rain")

for i in range(1,n):

    if min_a.nm > agents[i].nm and agents[i].lc  == "Rain":

        min_a = agents[i]

print(min_a.nm , min_a.bj, min_a.lc)