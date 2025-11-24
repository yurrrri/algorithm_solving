import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

answer = 0
start_x, start_y = 0, 0

board = []
for i in range(n):
  board.append(input())
  for j in range(m):
    if board[i][j] == "I":
      start_x = i
      start_y = j

def dfs(x, y):
  global answer
  
  visited[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] != "X":
      if board[nx][ny] == "P":
        answer += 1
      dfs(nx, ny)

dfs(start_x, start_y)
print(answer if answer != 0 else "TT")