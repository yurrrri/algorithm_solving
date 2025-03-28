def solution(id_list, report, k):
    result = []
    count_dic = {id: 0 for id in id_list}   # 신고당한 횟수를 담을 딕셔너리
    report_dic = {id: set() for id in id_list}  # 각 유저마다 신고한 유저를 담을 딕셔너리

    for r in report:
        reporter, reported = r.split()
        if reported not in report_dic[reporter]:
            report_dic[reporter].add(reported)
            
    for reporters in report_dic.values():
        for reported in reporters:
            count_dic[reported] += 1

    for key, v in report_dic.items():
        if len(v) == 0:
            result.append(0)
            continue
        count = 0
        for reported in v:
            if count_dic[reported] >= k:
                count += 1
        result.append(count)

    return result