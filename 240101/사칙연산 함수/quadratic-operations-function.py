def game(a,o,c):

    if o == '+':
        num = a + c
    elif o == '-':
        num = a - c
    elif o == '/':
        num = a // c
    elif o == '*' :
        num = a * c
    else : 
        print("False")
        return 

    print("{} {} {} = {}".format(a,o,c,int(num)))

arr = input().split()

a,o,c = int(arr[0]), arr[1], int(arr[2])

game(a,o,c)