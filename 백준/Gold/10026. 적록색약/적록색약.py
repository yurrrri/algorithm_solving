import copy
import sys

sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(visited, board, x, y, c):
  visited[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == c:
      dfs(visited, board, nx, ny, c)
      

n = int(input())
board1 = [list(input()) for _ in range(n)]
board2 = copy.deepcopy(board1)

visited = [[False] * n for _ in range(n)]

notWeakColor = 0
weakColor = 0

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(visited, board1, i, j, board1[i][j])
      notWeakColor += 1

    if board2[i][j] == "R":
      board2[i][j] = "G"

visited = [[False] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(visited, board2, i, j, board2[i][j])
      weakColor += 1

print(notWeakColor, weakColor)