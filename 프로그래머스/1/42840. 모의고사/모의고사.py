def solution(answers):
    answer = []
    member = [0]*3
    
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    for i, answer1 in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer1 == pattern[i%len(pattern)]:
                member[j] += 1
                
    
    max_number = max(member)
    
    
    for i, score in enumerate(member):
        if member[i] == max_number:
            answer.append(1+i)
    
    return answer