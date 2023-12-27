arr = input().split()

ch = arr[0]

ch = list(ch)

q = int(arr[1])

for i in range(q):

    arr = input().split()

    num = int(arr[0])

    if num == 1 :
        a = int(arr[1])
        b = int(arr[2])

        if a > b :
            c = ch[b-1]
            d = ch[a-1]

            for i in range(len(ch)) :
                if i == (b-1) :
                    ch[b-1]=d

                if i == (a-1) :
                    ch[a-1]=c 
            
            print(''.join(ch))
        
        else :
            c = ch[a-1]
            d = ch[b-1]

            for i in range(len(ch)) :
                if i == (a-1) :
                    ch[a-1]=d

                if i == (b-1) :
                    ch[b-1]=c 
            
            print(''.join(ch))
    
    else :

        a = arr[1]
        b = arr[2]

        for i in range(len(ch)) :
            if ch[i] == a :
                ch[i] = b

        print(''.join(ch))