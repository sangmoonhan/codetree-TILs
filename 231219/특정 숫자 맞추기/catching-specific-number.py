while True:
    n = input()
    n = int(n)
    if n < 25:
        print("Higher")
    elif n > 25 :
        print("Lower")
    else:
        print("Good")
        break