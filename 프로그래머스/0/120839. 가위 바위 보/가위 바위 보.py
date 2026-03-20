def solution(rsp):
    answer = ''
    r = list(rsp)
    
    for i in r:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
    return answer