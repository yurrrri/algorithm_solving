from collections import Counter

def solution(want, number, discount):
    want_dic = {}
    answer = 0
    flag = False
    
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    for i in range(len(discount)):  # 할인행사하는 맨 마지막날에 회원가입할수도 있으므로 discount 길이 전체 순회
        flag = False
        
        if i+10 >= len(discount):
            k = len(discount)
        else:
            k = i + 10
        
        dic = Counter(discount[i:k])
                        
        for w in want:   # 항목에 없거나 살 수 있는 수량이 부족하면 break
            if w not in dic or dic[w] < want_dic[w]:
                flag = True
                break
            
        if not flag:
            answer += 1
        
    return answer