ch = input()

for i in ch :
    if 'a' <= i and i <= 'z' :
        print(i.upper(),end="")
    else :
        print(i.lower(),end="")