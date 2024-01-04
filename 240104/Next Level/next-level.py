class game:
    def __init__(self,idx="codetree",lv=10):
        
        self.idx = idx
        self.lv = lv

obj1 = game()        

arr = list(input().split())

arr[1]= int(arr[1])

obj2 = game(arr[0],arr[1])

print("user", obj1.idx, "lv", obj1.lv)
print("user", obj2.idx, "lv", obj2.lv)