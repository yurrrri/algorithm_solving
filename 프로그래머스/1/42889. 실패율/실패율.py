def solution(N, stages):
    bunmo = len(stages)  # 처음 분모 stages의 길이로 시작
    counts = [0] * (N+2) # 분자 저장할 리스트
    dic = {} 
    
    for stage in stages:
        counts[stage] += 1
        
    for i in range(1, N+1):
        if counts[i] == 0:
            dic[i] = 0
        else:
            dic[i] = counts[i] / bunmo
            bunmo -= counts[i]
            
    print(dic)
            
    return sorted(dic, key=lambda x:dic[x], reverse=True)