import math

def solution(n):
    i = 1
    while math.factorial(i) <= n:
        i += 1
    
    answer = i-1
    return answer