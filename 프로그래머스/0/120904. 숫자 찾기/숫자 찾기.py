def solution(num, k):
    list_num = list(str(num))
    k = str(k)
    answer = 0
    
    if k in list_num:
        answer = list_num.index(k) +1
    else: 
        answer = -1
    return answer