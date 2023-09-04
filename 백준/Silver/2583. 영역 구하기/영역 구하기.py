from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)] # 가로: n, 세로: m
visited = [[0] * n for _ in range(m)] # 가로: n, 세로: m
# 색칠 되었거나 이미 판단한 영역 --> visited = 1, 빈칸을 visited = 0
for _ in range(k):
  a, b, c, d = map(int, input().split())
  for i in range(b, d):
    for j in range(a, c):
      board[i][j] = 1
      visited[i][j] = 1

def bfs(x, y):
  count = 1
  q = deque([(x, y)])
  visited[x][y] = 1

  while q:
    a, b = q.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
        count += 1
        visited[nx][ny] = 1
        q.append((nx, ny))

  return count

answer = []
area_count = 0
for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      area_count += 1
      answer.append(bfs(i, j))
      
print(area_count)
for i in sorted(answer):
    print(i, end=' ')