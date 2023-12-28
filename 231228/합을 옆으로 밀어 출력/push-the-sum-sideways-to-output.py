n = int(input())

sum_val = 0

for _ in range(n) :

    a = int(input())

    sum_val += a

ch = str(sum_val)

ch = ch[1:] + ch[0]

print(ch)