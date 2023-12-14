p1 = input().split()
p2 = input().split()
p3 = input().split()

g1 = p1[0]
g2 = p2[0]
g3 = p3[0]

c1 = int(p1[1])
c2 = int(p2[1])
c3 = int(p3[1])

if g1 == "Y" and c1 >= 37 :
    if g2 == "Y" and c2 >= 37 :
        print("E")
    elif g3 == "Y" and c3 >= 37 :
        print("E")
    else : print("N")
else : 
    if g2 == "Y" and c2 >= 37 :
        if g3 == "Y" and c3 >= 37:
            print("E")
        else :
            print("N")
    else :
        print("N")