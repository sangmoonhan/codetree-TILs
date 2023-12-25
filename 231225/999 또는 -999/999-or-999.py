arr = list(map(int,input().split()))

min_val = arr[0]
max_val = arr[0]

for elem in arr[1:]:
    
    if elem == 999 or elem == -999:
        break
    
    if min_val > elem:
        min_val = elem
        
    if max_val < elem:
        max_val = elem

print(max_val,min_val)