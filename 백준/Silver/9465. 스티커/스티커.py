import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  dp = []
  num = int(input())
  for _ in range(2):
    dp.append(list(map(int, input().split())))

  # DP[i][j]: i행, j열까지 도달했을 때의 최대값

  if num==1:
    print(max(dp[0][0], dp[1][0]))
  else:
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, num):
      dp[0][i] = dp[0][i] + max(dp[1][i-1], dp[1][i-2])
      dp[1][i] = dp[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][num-1], dp[1][num-1]))