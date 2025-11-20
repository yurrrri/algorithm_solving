import sys
sys.setrecursionlimit(10**8)

n, m, k = map(int, input().split())
board = [[0] * (m+1) for _ in range(n+1)]
visited = [[False] * (m+1) for _ in range(n+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(k):
  r, c = map(int, input().split())   # 음식물 쓰레기의 위치
  board[r][c] = 1
answer = 0

def dfs(x, y):
  cnt = 1
  visited[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1<=nx<=n and 1<=ny<=m and board[nx][ny] and not visited[nx][ny]:
      cnt += dfs(nx, ny)

  return cnt

for i in range(1, n+1):
  for j in range(1, m+1):
    if board[i][j] and not visited[i][j]:
      answer = max(answer, dfs(i, j))

print(answer)