arr = list(map(int,input().split()))

a = arr[0]

b = arr[1]

cnt = [0]*b

while a > 1 :
    cnt[a % b] += 1
    a = a // b

sum_val = 0 

for i in cnt :
    sum_val += i ** 2

print(sum_val)