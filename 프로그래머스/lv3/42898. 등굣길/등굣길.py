def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)] # n*m 배열 생성
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles: # 오답노트 1. 물웅덩이는 1개 이상임 -> 일치가 아닌 포함인지를 따져야함
                                  # 문제에서 주어진 좌표와 코딩할때의 배열 좌표가 서로 역전되어있음을 주의해야함
                                  # 문제에서 학교위치가 (m, n)이라고 나와있음
                continue
            
            if i == 1:
                dp[i][j] = dp[i][j-1]
            elif j == 1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    # DFS로 푸는 방법(재귀)
            

    return dp[n][m] % 1000000007