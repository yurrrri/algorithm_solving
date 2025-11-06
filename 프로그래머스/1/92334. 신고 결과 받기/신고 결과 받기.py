from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_history = defaultdict(set)
    reported_history = defaultdict(set)
    
    for r in report:
        reporter, reported = r.split()
        report_history[reporter].add(reported)
        reported_history[reported].add(reporter)
        
    for id in id_list:
        count = 0
        for reported in report_history[id]:
            if len(reported_history[reported]) >= k:
                count += 1
                
        answer.append(count)
    
    return answer