def solution(array, commands):
    answer = []
    for command in commands:
        new_answer = sorted(array[command[0]-1:command[1]])
        
        answer.append(new_answer[command[2]-1])
        print(command[2])
        
        
    return answer