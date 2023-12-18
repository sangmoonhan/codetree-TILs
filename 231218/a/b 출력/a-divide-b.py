arr = input().split()

a = 10 * int(arr[0])
b = int(arr[1])

#print(a/b)
print("0.",end="")
for i in range(0,20):
    c = a//b
    print(c,end="")
    a = 10 *(a%b)