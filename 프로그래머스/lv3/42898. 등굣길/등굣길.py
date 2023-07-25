def solution(m, n, puddles):
    #1) DP로 푸는 방법
    dp = [[0] * (m+1) for _ in range(n+1)] # n*m 배열 생성
    # dp[1][1] = 1
    
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if i == 1 and j == 1:
#                 continue
#             if [j, i] in puddles: # 오답노트 1. 물웅덩이는 1개 이상임 -> 일치가 아닌 포함인지를 따져야함
#                                   # 문제에서 주어진 좌표와 코딩할때의 배열 좌표가 서로 역전되어있음을 주의해야함
#                                   # 문제에서 학교위치가 (m, n)이라고 나와있음
#                 continue
            
#             if i == 1: # 맨 왼쪽이나 맨 위는 오른쪽이나 아래에서 오는 경우의수만 존재하므로 이전의 값을 그대로 가져옴
#                 dp[i][j] = dp[i][j-1]
#             elif j == 1:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1] # 그 외는 오른쪽과 아래에서 오는 경우의 수를 더함
    # return dp[n][m] % 1000000007  
    
    # 2) DFS로 푸는 방법(그래프 탐색)
    nx = 0
    ny = 0
    
    dx = [1, 0]
    dy = [0, 1]
    
    def dfs(x, y):        
        if x == n and y == m:
            return 1
        if dp[x][y] != 0:
            return dp[x][y]
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 1<=nx<=n and 1<=ny<=m:
                if [ny, nx] in puddles: continue
                dp[x][y] += dfs(nx, ny)
            
        return dp[x][y] % 1000000007
    
    return dfs(1, 1)