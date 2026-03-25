def solution(quiz):
    answer = []
    
    for q in quiz:
        a, op, b, _, c = q.split()
        
        a = int(a)
        b = int(b)
        c = int(c)
        
        if op == "+":
            result = a + b
        else:
            result = a - b
        
        if result == c:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer