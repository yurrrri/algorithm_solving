def solution(want, number, discount):
    want_dic = {}
    answer = 0
    flag = False
    
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    for i in range(len(discount)):
        dic = {}
        flag = False
        
        if i+10 >= len(discount):
            k = len(discount)
        else:
            k = i + 10
        for j in range(i, k):
            if discount[j] not in dic:
                dic[discount[j]] = 1
            else:
                dic[discount[j]] += 1
                        
        for w in want:
            if w not in dic or dic[w] < want_dic[w]:
                flag = True
                break
            
        if not flag:
            answer += 1
        
    return answer