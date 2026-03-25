def solution(num, total):
    start = total // num - (num - 1) // 2
    answer = []
    
    for i in range(num):
        answer.append(start + i)
    
    return answer