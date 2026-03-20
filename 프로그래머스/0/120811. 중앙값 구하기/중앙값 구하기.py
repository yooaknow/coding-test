def solution(array):
    answer = 0
    a = sorted(array)
    n = len(a)
    q = n//2
    
    answer = a[q]
    
    return answer