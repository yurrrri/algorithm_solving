from collections import Counter

def solution(N, stages):
    counter = dict(Counter(stages))
    count = len(stages)
    
    dic = {}
    
    for i in range(1, N+1):
        if i not in counter.keys():
            dic[i] = 0
            continue
        dic[i] = counter[i] / count
        count -= counter[i]
        
    answer = sorted(dic, key=lambda x:dic[x], reverse=True)
        
    return answer