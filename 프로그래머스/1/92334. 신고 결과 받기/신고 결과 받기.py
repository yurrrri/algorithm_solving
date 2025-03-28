def solution(id_list, report, k):
    result = []
    count_dic = {}   # 신고당한 횟수를 담을 딕셔너리
    report_dic = {}  # 각 유저마다 신고한 유저를 담을 딕셔너리
    for id in id_list:  # 초기화
        count_dic[id] = 0
        report_dic[id] = []
    
    for r in report:
        reporter, reported = r.split()
        if reported not in report_dic[reporter]:
            report_dic[reporter].append(reported)
            count_dic[reported] += 1

    for key, v in report_dic.items():  #(10^3)
        if len(v) == 0:
            result.append(0)
            continue
        count = 0
        for reported in v:
            if count_dic[reported] >= k:
                count += 1
        result.append(count)
    
    return result