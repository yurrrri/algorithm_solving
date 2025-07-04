def solution(n, stations, w):
    answer = 0
    aparts = range(1, n+1)   # 1부터 n까지의 배열
    idx = 1           # 현재 탐색하는 아파트 위치
    station_idx = 0   # 설치된 기지 위치
    
    while idx <= n:
        if station_idx < len(stations) and idx >= stations[station_idx] - w:   # 이미 설치되어있는 기지국의 전파의 범위에 닿을 경우,
            idx = stations[station_idx] + w + 1   # 전파되지 않은 범위로 이동
            station_idx += 1     
        else:               # 이미 설치되어 있는 기지국의 전파 범위가 아닐 경우
            idx += 2 * w + 1    # 기지국 설치 후, 그 다음 전파가 닿지 않는 범위로 이동
            answer += 1
    
    return answer