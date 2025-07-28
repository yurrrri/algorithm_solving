def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n <= 3:
        return max(sticker)
    
    dp = [[0] * n for _ in range(2)]  # dp의 해: 스티커에 적힌 숫자의 합의 최대값
    # dp[0]: 첫번째 스티커를 뗸 경우, dp[1]: 첫번째 스티커를 떼지 않은 경우
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]           # 첫번째 스티커를 이미 뗐으므로, 인접한 그 다음 칸은 그 전의 해와 같다.
    
    dp[1][0] = 0 
    dp[1][1] = sticker[1]
    
    # 첫번째 스티커를 뜯으면서 시작한 경우
    for i in range(2, n-1):
        dp[0][i] = max(dp[0][i-1], dp[0][i-2] + sticker[i])  # 차례대로 스티커를 떼지 않는 경우, 스티커를 떼는 경우
    
    # 첫번째 스티커를 떼지 않은 경우
    for i in range(2, n):
        dp[1][i] = max(dp[1][i-1], dp[1][i-2] + sticker[i])
        
    return max(dp[0][-2], dp[1][-1])