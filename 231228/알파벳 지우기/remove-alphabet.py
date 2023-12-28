sum_val = 0

for i in range(2):

    ch = input()

    num = ""

    for j in ch :
        if j.isdigit():

            num += j
    
    sum_val += int(num)

print(sum_val)