from collections import defaultdict

def solution(gems):
    gem_set = set(gems) # 중복 제거 (최소한 1개 이상만 있으면 되니까)
    dic = defaultdict(int)
    answer = []  # 구간을 저장해두고 나중에 정렬
    n = len(gems)
    
    start = 0
    end = 0
    
    dic[gems[start]] = 1
    
    while end < n:
        if len(dic) < len(gem_set): # 보석 종류가 모자라다면, end 포인터 이동하면서 보석 추가
            end += 1
            if end >= n:
                break
            dic[gems[end]] += 1
        else: # 만약에 모든 종류의 보석을 다 모았다면, 최소 구간을 구해야함
            answer.append([start+1, end+1])
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
    
    answer.sort(key=lambda x:((x[1]-x[0]), x[0]))
    
    return answer[0]