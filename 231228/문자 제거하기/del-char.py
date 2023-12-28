ch = input()

while len(ch) != 1 :

    n = int(input())

    if n >= len(ch) :
        ch = list(ch)
        ch.pop()
        ch = ''.join(ch)
        print(ch)
    else:
        ch = list(ch)
        ch.pop(n)
        ch = ''.join(ch)
        print(ch)