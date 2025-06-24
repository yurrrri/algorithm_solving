import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * n for _ in range(n)]
    
    q = []
    heapq.heappush(q, (0, 0, 0))
    
    while q:
        cost, x, y = heapq.heappop(q)
        
        if visited[x][y]:
            continue
            
        answer += cost
        visited[x][y] = True
        
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