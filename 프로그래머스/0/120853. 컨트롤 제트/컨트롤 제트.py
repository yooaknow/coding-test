def solution(s):
    answer = 0
    s = s.split()
    result = 0
    minus = 0
    for i in s:
        if i != "Z":
            result += int(i)
            minus = int(i)
        elif i == "Z":
            result -= minus
    answer = result
    return answer