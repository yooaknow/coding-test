def solution(id_list, report, k):
    report = set(report)
    my_dict = {id_name: [] for id_name in id_list}
    report_count = {id_name: 0 for id_name in id_list}
    
    for i in report:
        i = i.split(" ")
        user = i[0]     
        reported = i[1]  
        
        my_dict[user].append(reported)
        report_count[reported] += 1
        
    answer = []
    for id_name in id_list:
        mail = 0
        for reported_user in my_dict[id_name]:
            if report_count[reported_user] >= k:
                mail += 1
        answer.append(mail)

    return answer