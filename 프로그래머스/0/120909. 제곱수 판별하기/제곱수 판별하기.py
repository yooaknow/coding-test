def solution(n):
    answer = 0
    a = int(n**0.5)
    if a*a == n:
        answer = 1
    else: 
        answer = 2
    return answer