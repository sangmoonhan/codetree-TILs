def is_yoon(n):
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    if n % 4 == 0 and n % 100 == 0 :
        return False
    if n % 4 == 0:
        return True
    return True

n = int(input())

if is_yoon(n) :
    print('true')
else :
    print('false')