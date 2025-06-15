def solution(n, stations, w):
    idx = 0     # 기지국이 설치되어있는 인덱스
    location = 1   # 현재 위치
    answer = 0
    
    while location <= n:
        if idx < len(stations) and location >= stations[idx] - w:  # 전파가 닿아있는 범위를 보면 건너뛰어야함
            location = stations[idx] + w + 1
            idx += 1
        else:     # 닿아있지 않다면 전파 설치
            answer += 1
            location += 2 * w + 1  # 해당 기지국을 설치함으로써 전파가 닿지않는 범위로 이동
            
    return answer