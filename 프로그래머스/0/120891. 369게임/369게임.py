def solution(order):
    answer = 0
    a = str(order)
    
    for ch in a:
        if ch in "369":
            answer += 1
    return answer