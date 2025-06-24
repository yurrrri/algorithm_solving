import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * n for _ in range(n)]
    
    """
    우선순위 큐 사용 이유 --> 사다리 설치 비용을 최소로 한다는것은 인접한 칸끼리의 비용이 최소인 순서대로 방문해야하기 때문에
    pop을 할때마다 최소값을 보장해주는 우선순위 큐 사용
    """
    q = []
    heapq.heappush(q, (0, 0, 0))
    
    while q:
        cost, x, y = heapq.heappop(q)
        
        if visited[x][y]:
            continue
            
        answer += cost            # 사다리를 설치했다면 차이 비용일 것이고, 아니라면 0일 것임 (영향 X)
        visited[x][y] = True      # 최소 비용으로 선택한 다음 노드에 대해 방문처리
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                new_cost = abs(land[x][y] - land[nx][ny])
                
                if new_cost > height:
                    heapq.heappush(q, (new_cost, nx, ny))
                else:
                    heapq.heappush(q, (0, nx, ny))
            
    return answer