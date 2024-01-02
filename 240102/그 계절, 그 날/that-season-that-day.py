def is_yoon(n):
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    if n % 4 == 0 and n % 100 == 0 :
        return False
    if n % 4 == 0:
        return True
    return False

def mon_day(y,m,d):

    if is_yoon(y):

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
            if 1 <= d <= 29:
                return True
            else :
                return False
        else:
            return False
    else :

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

y, m, d = tuple(map(int,input().split()))

if mon_day(y, m, d):
    if m in [12,1,2]:
        print("Winter")
    elif m in [3,4,5]:
        print("Spring")
    elif m in [6,7,8]:
        print("Summer")
    else :
        print("Fall")
else :
    print(-1)