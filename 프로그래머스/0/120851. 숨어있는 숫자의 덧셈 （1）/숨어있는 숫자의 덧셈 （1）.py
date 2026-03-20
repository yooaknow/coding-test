def solution(my_string):
    answer = 0
    a = list(my_string)
    for ch in a:
        if ch.isdigit():
            answer += int(ch)
    return answer