def solution(my_string):
    answer = ''
    a= my_string.lower()
    b = sorted(a)
    answer = "".join(b)
    return answer