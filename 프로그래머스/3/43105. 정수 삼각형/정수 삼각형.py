def solution(triangle):
    n = len(triangle[-1])
    if n == 1:
        return triangle[0][0]
    
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]             # 기본값 설정
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]
    
    for i in range(2, n):      # 점화식 세우기
        for j in range(i+1):
            if j == 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]   # 왼쪽은 왼쪽에서만 내려옴
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]   # 오른쪽은 오른쪽에서만 내려옴
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]  # 이전 dp의 왼쪽, 오른쪽 비교
    return max(dp[n-1])