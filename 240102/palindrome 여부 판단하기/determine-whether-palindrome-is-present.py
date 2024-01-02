def refle(ch):
    ch1 = ch
    ch2 = ch[::-1]

    if ch1 == ch2:
        print("Yes")
    else:
        print("No")

ch = input()

refle(ch)