def solution(progresses, speeds):
    answer = []
    blank = []  
    
    for i, j in zip(progresses, speeds):
        x = 1  
        while i + (j * x) < 100:
            x += 1
            
        blank.append(x)
        
    current_max = blank[0]
    count = 1
    
    for k in range(1, len(blank)):
        if blank[k] <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = blank[k]
            count = 1
    answer.append(count)
    return answer