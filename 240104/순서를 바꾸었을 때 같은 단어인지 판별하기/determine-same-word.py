a= input()
b= input()

a= ''.join(sorted(a))
b= ''.join(sorted(b))

if a == b :
    print("Yes")
else:
    print("No")