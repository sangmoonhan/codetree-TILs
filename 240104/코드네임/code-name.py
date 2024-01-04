class Agent:
    def __init__(self, nm, sc=0):
        self.nm = nm
        self.sc = sc
        

agents = []
for _ in range(5):
    nm, sc = tuple(input().split())
    sc = int(sc)
    agents.append(Agent(nm, sc))

min_a = agents[0]

for i in range(1,5):

    if min_a.sc > agents[i].sc:

        min_a = agents[i]

print(min_a.nm, min_a.sc)