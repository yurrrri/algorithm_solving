import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]  # 거리를 저장할 DP 테이블

dx = [-1, 1, 0, 0]   # 좌, 우, 하
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x == m-1 and y == n-1:
    return 1

  if dp[x][y] != -1:
    return dp[x][y]

  dp[x][y] = 0
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<m and 0<=ny<n and board[x][y] > board[nx][ny]:
      dp[x][y] += dfs(nx, ny)

  return dp[x][y]

print(dfs(0, 0))