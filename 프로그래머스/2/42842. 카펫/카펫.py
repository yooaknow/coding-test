def solution(brown, yellow):
    answer = []
    plus = brown + yellow
    
    for i in range(1,plus+1):
        quotient = plus // i
        
        if (quotient*i == plus and (quotient-2)*(i-2) == yellow and quotient>=i):
            answer.append(quotient)
            answer.append(i)
    
    return answer


    