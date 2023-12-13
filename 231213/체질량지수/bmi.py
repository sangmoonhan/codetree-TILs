arr= input().split()

a = int(arr[0])
b = int(arr[1])

a *= 0.01

print(int(b//(a*a)))

if b//(a*a) > 25:
    print("Obesity")