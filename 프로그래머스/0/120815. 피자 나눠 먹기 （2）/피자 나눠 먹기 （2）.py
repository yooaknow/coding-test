def solution(n):
    answer = ""
    a= list(answer)
    for i in range(1,n+1):
        if (6*i) % n == 0:
            a.append(i)
            answer = a[0]
    return answer