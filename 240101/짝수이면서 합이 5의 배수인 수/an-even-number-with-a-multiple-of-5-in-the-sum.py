def is_num(n):

    a = n // 10
    b = n % 10

    if n % 2 == 0 and ( a + b ) % 5 == 0 : 
        return "Yes"
    else :
        return "No"

n = int(input())

print(is_num(n))