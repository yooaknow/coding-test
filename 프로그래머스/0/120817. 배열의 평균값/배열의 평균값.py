def solution(numbers):
    a = 0
    answer=0
    n = len(numbers)
    
    for i in range(n):
        a += numbers[i]
    
    answer = a / n
    return answer