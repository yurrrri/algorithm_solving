answer = -1

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(power, num):
        global answer
        
        answer = max(answer, num)   # 탐험할 수 있는 최대 던전 수 갱신
        
        for i in range(len(dungeons)):
            if not visited[i] and power >= dungeons[i][0]:  # 방문하지 않은 던전 중, 현재 피로도에서 방문할 수 있는 던전이라면
                visited[i] = True       # 해당 던전 방문처리 후
                dfs(power - dungeons[i][1], num+1)    # 피로도 소모 및 방문갯수 count + 1
                visited[i] = False      # 해당 던전 방문여부를 복원하여 다른 후보지 탐색
                
    dfs(k, 0)
        
    return answer