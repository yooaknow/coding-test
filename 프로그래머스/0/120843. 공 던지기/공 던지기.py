def solution(numbers, k):
    k = k-1
    a= 1+ k*2
    answer = 0
    numbers = len(numbers)
    answer = a%numbers
    if answer == 0:
        answer = numbers
        
    return answer