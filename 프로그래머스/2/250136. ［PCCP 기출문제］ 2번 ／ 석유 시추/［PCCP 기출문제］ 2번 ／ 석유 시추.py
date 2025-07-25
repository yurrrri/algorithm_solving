import sys
sys.setrecursionlimit(10**6)    # 재귀 깊이를 늘려줘야 런타임 에러가 안뜸

def solution(land):
    answer = 0
    n = len(land)   # n: 세로길이 - x
    m = len(land[0])  # m: 가로길이 - y
    visited = [[False] * m for _ in range(n)]
    cols = [0] * m
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x, y):
        nonlocal size
        
        visited[x][y] = True
        size += 1
        temp.add(y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)
                
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                temp = set()
                size = 0
                dfs(i, j)
                for y in temp:
                    cols[y] += size                
    
    return max(cols)