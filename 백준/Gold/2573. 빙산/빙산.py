from collections import deque

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
  visited[i][j] = True
  q = deque([(i, j)])

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == 0:
          count[x][y] += 1
        elif board[nx][ny] != 0 and not visited[nx][ny]:
          q.append((nx, ny))
          visited[nx][ny] = True
  for a in range(n):
    for b in range(m):
      board[a][b] -= count[a][b]
      if board[a][b] < 0:
        board[a][b] = 0
        
answer = 0
while True:
  visited = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)]
  area_count = 0
  
  for i in range(n):
    for j in range(m):
      if board[i][j] != 0 and not visited[i][j]:
        bfs(i, j)
        area_count += 1

  if area_count == 0:
    print(0)
    break
  elif area_count >= 2:
    print(answer)
    break

  answer += 1