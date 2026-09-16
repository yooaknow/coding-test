def solution(nums):
    answer = 0
    x = set(nums)
    x = len(x)
    y = len(nums)//2
    
    if (x<=y):
        answer = x
    else:
        answer = y
    return answer