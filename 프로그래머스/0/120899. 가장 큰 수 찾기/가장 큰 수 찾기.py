def solution(array):
    answer = []
    m = max(array)
    n=0
    
    for i in range(len(array)):
        if array[i]== m:
            n=i
    answer.append(m)
    answer.append(n)
    return answer