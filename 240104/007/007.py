class game:
    def __init__(self,sc,mp,tm):
        
        self.sc = sc
        self.mp = mp
        self.tm = tm

arr = list(input().split())

arr[2]= int(arr[2])

obj = game(arr[0],arr[1],arr[2])

print("secret code : {}".format(obj.sc))
print("meeting point : {}".format(obj.mp))
print("time : {}".format(obj.tm))