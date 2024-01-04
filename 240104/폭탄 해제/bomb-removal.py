class Agent:
    def __init__(self, cd, cl, sc):
        self.cd = cd
        self.cl = cl
        self.sc = sc
        
a,b,c = tuple(input().split())

c = int(c)

arr = Agent(a,b,c)

print("code : {}".format(arr.cd))
print("color : {}".format(arr.cl))
print("second : {}".format(arr.sc))