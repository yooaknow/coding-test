def solution(s):
    if len(s) == 1:
        return 1

    c = []

    for j in range(1, len(s)):
        blank = []
        a = 1

        slicing = [s[i:i+j] for i in range(0, len(s), j)]

        for i in range(1, len(slicing)):
            if slicing[i-1] == slicing[i]:
                a += 1
            else:
                if a == 1:
                    blank.append(slicing[i-1])
                else:
                    blank.append(str(a) + slicing[i-1])
                a = 1

        if a == 1:
            blank.append(slicing[-1])
        else:
            blank.append(str(a) + slicing[-1])

        blank = ''.join(blank)
        c.append(blank)

    return len(min(c, key=len))