arr = int(input())

arr = list(map(int,list(str(arr)[::-1])))

num = 1

sum_val = 0

for i in arr :

    sum_val += num * i

    num *= 2

print(sum_val)