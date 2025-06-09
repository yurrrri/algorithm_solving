def solution(money):
    n = len(money)
    dp1 = [0] * n   # 첫번째 집 방문했을 때, n번 집까지 방문했을 때의 최대값
    dp2 = [0] * n   # 첫번째 집을 방문하지 않았을 때, n번 집까지 방문했을 때의 최대값
    
    dp1[0] = money[0]
    dp1[1] = money[0]    # 첫번째 집 방문했으므로, 인접한 집은 털 수 없으므로 두번째 집까지의 방문 최대값은 첫번째 집 털이임
    for i in range(2, n-1):    # 첫번째 집 방문했으므로 마지막 집 제외하고 점화식 실행
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    dp1[n-1] = dp1[n-2]    # 마지막 집은 털 수 없으므로 그 전 집까지 방문했을 때가 최대값임
    
    dp2[1] = money[1]    # 첫번째 집 방문 X
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    
    return max(dp1[-1], dp2[-1])