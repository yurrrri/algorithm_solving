from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
board = []

for i in range(n):
  board.append(list(input()))

answer = 0
def bfs(i, j):
  q = deque([])
  q.append((i, j))
  visited = [[0] * m for _ in range(n)]
  visited[i][j] = 1
  count = 0
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and board[nx][ny] == "L" and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
        count = max(count, visited[nx][ny])

  return count-1  # 두 최단 거리 사이의 거리이므로 -1을 해줘야함

for i in range(n):
  for j in range(m):
    if not visited[i][j] and board[i][j] == "L":
      answer = max(answer, bfs(i, j))

print(answer)