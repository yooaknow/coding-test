def solution(money):
    answer = []
    count = money // 5500
    n = money- count * 5500
    answer.append(count)
    answer.append(n)
    return answer