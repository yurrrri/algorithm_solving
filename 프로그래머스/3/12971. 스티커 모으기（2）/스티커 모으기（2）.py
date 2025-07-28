def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    
    dp[1][1] = sticker[1]
    
    # 첫번째 스티커를 뜯으면서 시작한 경우
    for i in range(2, n-1):
        dp[0][i] = max(dp[0][i-1], dp[0][i-2] + sticker[i])
    
    # 두번째 스티커를 뜯으면서 시작한 경우
    for i in range(2, n):
        dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])
        
    return max(max(dp[0]), max(dp[1]))