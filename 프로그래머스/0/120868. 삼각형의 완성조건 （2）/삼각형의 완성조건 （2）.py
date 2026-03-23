def solution(sides):
    answer = 0
    min_side = min(sides)
    max_side = max(sides)
    
    minx= max_side - min_side +1
    maxx= max_side + min_side -1
    
    answer = maxx-minx +1
    return answer