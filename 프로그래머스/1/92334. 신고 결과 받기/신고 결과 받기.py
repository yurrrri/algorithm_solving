from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report_dic = defaultdict(set)
    reported_dic = {x: 0 for x in id_list}
    
    for r in report:
        user, reported = r.split()
        report_dic[user].add(reported)
        
    for _id in id_list:
        for reported in report_dic[_id]:
            reported_dic[reported] += 1
            
    for _id in id_list:
        _sum = 0
        for reported in report_dic[_id]:
            if reported_dic[reported] >= k:
                _sum += 1
                
        answer.append(_sum)
    
    return answer