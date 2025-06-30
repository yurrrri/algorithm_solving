from itertools import permutations

def solution(n, weak, dist):
    answer = 9
    _len = len(weak)
    
    for i in range(_len):
        weak += [weak[i] + n]
        
    
    # 2. 모든 취약점 위치를 시작점으로 하여 각 친구가 취약 지점들을 커버할 수 있는지 확인함
    for i in range(_len):
        for friend in permutations(dist, len(dist)):
            cnt = 1
            pos = weak[i] + friend[cnt - 1]    # 첫번째 친구가 i 위치의 취약점에서 이동할 수 있는 거리
            for j in range(i, i + _len):
                if pos < weak[j]:       # i 이후의 각 취약점을 현재 친구가 커버할 수 없으면, 친구를 추가 투입해야함
                    cnt += 1
                    if cnt > len(dist):
                        break
                        
                    pos = weak[j] + friend[cnt-1]
                    
            answer = min(answer, cnt)
    
    return answer if answer <= len(dist) else -1