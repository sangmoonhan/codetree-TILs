a, b = tuple(map(int,input().split()))

arr = int(input())

arr = list(map(int,list(str(arr)[::-1])))

num = 1

sum_val = 0

for i in arr :

    sum_val += num * i

    num *= a

n = int(sum_val)

digits = []

while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b

# print binary number
for digit in digits[::-1]:
    print(digit, end="")