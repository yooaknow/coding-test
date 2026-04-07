def solution(array, commands):
    answer = []
    
    for i in commands:

        slice_array = array[i[0]-1: i[1]]
        sort = sorted(slice_array)
        answer.append(sort[i[2]-1])
        
        
    return answer