class Agent:
    def __init__(self, cd="codetree", sc=50):
        self.cd = cd
        self.sc = sc
        
a,b = tuple(input().split())

b = int(b)

arr = Agent()
brr = Agent(a,b)

print("product {} is {}".format(arr.sc,arr.cd))
print("product {} is {}".format(brr.sc,brr.cd))