from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
      
def bfs():
  q = deque([(0, 0)])
  visited[0][0] = 1
  count = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == 1:
          visited[nx][ny] += 1
        elif board[nx][ny] == 0 and not visited[nx][ny]:
          visited[nx][ny] = 1
          q.append((nx, ny))

  for i in range(n):
    for j in range(m):
      if visited[i][j] >= 2:
        board[i][j] = 0
        count += 1

  return count

answer = 0
while True:
  visited = [[0] * m for _ in range(n)]
  count = bfs()
  if count == 0:
    print(answer)
    exit()
  answer += 1