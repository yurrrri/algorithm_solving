def solution(land):
    n = len(land)
    m = len(land[0])
    dp = [[0] * m for _ in range(n)]
    dp[0] = land[0]
    
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                if j == k: continue
                dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    return max(dp[-1])