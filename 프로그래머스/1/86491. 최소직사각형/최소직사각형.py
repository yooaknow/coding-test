def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort(reverse=True)
        print(size) 
    
    max_x = max(size[0] for size in sizes)
    max_y = max(size[1] for size in sizes)
    
    answer = max_x * max_y

    return answer