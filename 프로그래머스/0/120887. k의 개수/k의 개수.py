def solution(i, j, k):
    answer = 0
    for num in range(i, j+1, 1):
        num = list(str(num)) 
        if str(k) in num:
            answer += num.count(str(k))
    return answer