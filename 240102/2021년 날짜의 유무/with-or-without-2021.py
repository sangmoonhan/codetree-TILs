def mon_day(m,d):

    if m in [1,3,5,7,8,10,12]:
        if 1 <= d <= 31:
            return True
        else :
            return False
    elif m in [4,6,9,11]:
        if 1 <= d <= 30:
            return True
        else :
            return False
    elif m == 2:
        if 1 <= d <= 28:
            return True
        else :
            return False
    else:
        return False

m, d = tuple(map(int,input().split()))

if mon_day(m, d):
    print("Yes")
else :
    print("No")