def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dx = [0, 1]  # 오른쪽과 아래로만 움직임
    dy = [1, 0]
    
    def dfs(x, y):
        if x == n and y == m:
            return 1
        
        if dp[x][y]:
            return dp[x][y]
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 1<=nx<=n and 1<=ny<=m and [ny, nx] not in puddles:
                dp[x][y] += dfs(nx, ny)
    
        return dp[x][y] % 1_000_000_007
    
    return dfs(1, 1)