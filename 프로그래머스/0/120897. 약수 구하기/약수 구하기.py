def solution(n):
    answer = []
    for i in range(n+1):
        for a in range(n+1):
            if a*i == n:
                answer.append(i)
    return answer