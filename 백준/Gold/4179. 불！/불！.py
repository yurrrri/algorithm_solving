from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []

R, C = map(int, input().split())
visited_f = [[-1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

fire_x, fire_y = 0, 0
jihoon_x, jihoon_y = 0, 0
q = deque([])

for i in range(R):
  board.append(input())
  for j in range(C):
    if board[i][j] == "J":
      jihoon_x, jihoon_y = i, j
    elif board[i][j] == "F":
      q.append((i, j))

# 불 먼저 이동
for x, y in q:
  visited_f[x][y] = 0

while q:
  x, y = q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if not (0<=nx<R and 0<=ny<C):
      continue

    if board[nx][ny] != "#" and visited_f[nx][ny] == -1:
      visited_f[nx][ny] = visited_f[x][y] + 1
      q.append((nx, ny))

# 지훈 이동
visited[jihoon_x][jihoon_y] = True
q = deque([(jihoon_x, jihoon_y, 0)])

while q:
  x, y, t = q.popleft()
    
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<R and 0<=ny<C:
      if board[nx][ny] == "." and not visited[nx][ny] and (visited_f[nx][ny] == -1 or t + 1 < visited_f[nx][ny]):
        visited[nx][ny] = True
        q.append((nx, ny, t+1))
    else:
      print(t+1)
      exit()

print("IMPOSSIBLE")