def solution(my_string):
    answer = 0
    a = []
    b = ""
    
    for ch in my_string:
        if ch.isdigit():
            b += ch
        else:
            if b != "":
                a.append(b)
                b = ""
                
    if b != "":
        a.append(b)
        
    for i in range(len(a)):
        answer += int(a[i])
    return answer