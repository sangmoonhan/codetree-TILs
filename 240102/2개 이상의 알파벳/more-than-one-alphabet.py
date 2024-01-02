def diffe(ch):

    ch = list(ch)

    cnt = 0

    for i in range(len(ch)):

        if i == 0 :
            cnt += 1
            continue

        if ch[i] in ch[:i] :
            continue
        else:
            cnt += 1
    
    if cnt >= 2 :
        return "Yes"
    else :
        return "No"

ch = input()

ch = diffe(ch)

print(ch)