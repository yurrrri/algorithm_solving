def solution(N, stages):
    bunmo = len(stages)  # 처음 분모 stages의 길이로 시작
    counts = [0] * (N+2) # 분자 저장할 리스트
    dic = {}  # 키 - 쌍: 딕셔너리 활용
    
    for stage in stages:
        counts[stage] += 1     # 먼저 반복문을 통해 값을 미리 저장해두기 (시간복잡도 줄이기)
        
    for i in range(1, N+1):
        if counts[i] == 0:
            dic[i] = 0
        else:
            dic[i] = counts[i] / bunmo
            bunmo -= counts[i]
                        
    return sorted(dic, key=lambda x:dic[x], reverse=True)  #딕셔너리 정렬 -> 키값만 반환한 리스트