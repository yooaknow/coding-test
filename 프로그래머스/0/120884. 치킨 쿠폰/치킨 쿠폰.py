def solution(chicken):
    answer = 0

    while chicken >= 10:
        service = chicken // 10     
        remain = chicken % 10   

        answer += service
        chicken = service + remain 

    return answer