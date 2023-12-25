n = int(input())

arr = list(map(int, input().split()))

if arr.count(max(arr)) >= 2 :
    print(max(arr),max(arr))
else:

    max_val = [max(arr)]
    max_val2= arr[0]

    for i in arr:
        
        if max_val[0] == i:
            continue
        
        else : 
            if max_val2 <= i :
                max_val2 = i

    max_val.append(max_val2)
    
    print(max_val[0],max_val[1])