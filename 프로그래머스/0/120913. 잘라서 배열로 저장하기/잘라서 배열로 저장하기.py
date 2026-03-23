def solution(my_str, n):
    answer = []
    count = 0
    array = []
    a = ""
    
    for i in my_str:
        a += i
        count += 1
        
        if count >= n:
            array.append(a)
            a = ""
            count = 0
    
    if a != "":
        array.append(a)

    answer = array
        
    return answer