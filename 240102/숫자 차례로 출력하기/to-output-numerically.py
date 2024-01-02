def print_seq1(n):  
    if n == 0:      
        return

    print_seq1(n - 1)
    print(n, end=" ")

def print_seq2(n):  
    if n == 0:      
        return

    print(n, end=" ")
    print_seq2(n - 1)
        

n = int(input())

print_seq1(n)
print()
print_seq2(n)