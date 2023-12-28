ch = input()

for i in ch :
    if i.isalpha() :
        print(i.lower(),end="")
    
    if i.isdigit() :
        print(i,end="")