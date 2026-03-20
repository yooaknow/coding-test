def solution(emergency):
    answer = []
    eme_list = sorted(emergency, reverse = True)
    
    for i in emergency:
        answer.append(eme_list.index(i)+1)
    return answer