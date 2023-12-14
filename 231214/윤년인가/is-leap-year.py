a = int(input())

if a % 4 == 0 :
    if a % 100 == 0 :
        if a % 400 == 0 :
            print("true")
        else :
            print("false")
    else :
        print("true")
else :
    print("false")