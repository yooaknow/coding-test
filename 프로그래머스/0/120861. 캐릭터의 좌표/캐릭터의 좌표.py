def solution(keyinput, board):
    answer = []
    max_x = board[0]//2
    max_y = board[1]//2
    x = 0
    y = 0
    
    for ch in keyinput:
        if ch == "left" and x > -max_x:
            x -= 1
        elif ch == "right" and x < max_x:
            x += 1
        elif ch == "up" and y < max_y:
            y += 1
        elif ch == "down" and y > -max_y:
            y -= 1
    
    answer.append(x)
    answer.append(y)
            
    return answer