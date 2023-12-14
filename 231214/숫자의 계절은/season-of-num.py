# 12 1 2 3 4 5 6 7 8 9 10 11
# 0 1 2 3 4 5 6 7 8 9 10 11
a=int(input())

a %= 12

if a >= 9 :
    print("Fall")
elif a>= 6 :
    print("Summer")
elif a>=3 :
    print("Spring")
else : 
    print("Winter")