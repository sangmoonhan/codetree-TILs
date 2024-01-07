arr = int(input())

arr = list(map(int,list(str(arr)[::-1])))

num = 1

sum_val = 0

for i in arr :

    sum_val += num * i

    num *= 2

sum_val *= 17

n = int(sum_val)

digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")