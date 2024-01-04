n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

jud = "Yes"

for i in range(n):
    if a[i] != b[i]:
        jud="No"

print(jud)