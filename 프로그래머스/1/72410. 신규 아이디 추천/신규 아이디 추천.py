def solution(new_id):
    answer = ''
    
    step1 = new_id.lower()
    step2 = ''
    
    for c in step1:
        if c.isalpha() or c.isdigit() or c in "-_.":
            step2+=c
            
    while '..' in step2:        
        step2=step2.replace('..', '.')
    
    step3 = step2.strip(".")
    
    if step3 == "":
        step3 = "a"
    else:
        step3 = step3
        
    if len(step3) >= 16:
        step3 = step3[:15]
        step3 = step3.rstrip(".")
        
    if len(step3) <= 2:
        while len(step3) < 3:
            step3 += step3[-1]
                
    answer = step3
    return answer