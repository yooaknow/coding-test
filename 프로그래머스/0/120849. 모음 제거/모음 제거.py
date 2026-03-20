def solution(my_string):
    answer = ''
    
    for n in my_string:
        if n not in "aeiou":
            answer += n
            
    return answer