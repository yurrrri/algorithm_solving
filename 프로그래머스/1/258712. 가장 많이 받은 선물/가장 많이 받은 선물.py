from collections import defaultdict

def solution(friends, gifts):
    present_count = defaultdict(int)
    dic1 = defaultdict(dict)    # 선물을 준 기록 딕셔너리
    dic2 = {}    # 각 프렌즈마다 준 선물, 받은 선물 갯수를 기록하는 딕셔너리
    for friend1 in friends:
        for friend2 in friends:
            if friend1 != friend2:
                dic1[friend1][friend2] = 0
                dic2[friend1] = [0, 0]

    for gift in gifts:
        giver, receiver = gift.split()
        dic1[giver][receiver] += 1
        dic2[giver][0] += 1
        dic2[receiver][1] += 1
        
    for friend1 in friends:
        for (friend2, v) in dic1[friend1].items():
            if dic1[friend1][friend2] > dic1[friend2][friend1]:
                present_count[friend1] += 1
            elif dic1[friend1][friend2] == dic1[friend2][friend1]:
                friend1_present_num = dic2[friend1][0] - dic2[friend1][1]
                friend2_present_num = dic2[friend2][0] - dic2[friend2][1]

                if friend1_present_num > friend2_present_num:
                    present_count[friend1] += 1

    return max(list(present_count.values())) if list(present_count.values()) else 0