def solution(array):
    answer = 0
    for ch in array:
        ch = str(ch)
        answer += ch.count('7')
    return answer