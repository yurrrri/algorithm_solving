n, k = map(int, input().split())
INF = int(1e9)
dp = [INF] * (n+1)
dp[0] = 0

for i in range(n):
  if i + 1 <= n:
    dp[i+1] = min(dp[i+1], dp[i] + 1)
  if i + i/2 <= n:
    dp[int(i + i/2)] = min(dp[int(i + i/2)], dp[i] + 1)

print("minigimbob" if dp[n] <= k else "water")