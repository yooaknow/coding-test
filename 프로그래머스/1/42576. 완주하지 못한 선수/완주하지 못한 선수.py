def solution(participant, completion):
    answer = ''
    Counts= {}
    
    for name in participant:
        Counts[name] = Counts.get(name,0)+1
    
    for name in completion:
        Counts[name] -= 1
        
    for name, key in Counts.items():
        if key>0:
            answer = name
    return answer