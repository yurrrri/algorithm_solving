from collections import deque

r, c = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start_x, start_y = 0, 0
end_x, end_y = 0, 0
INF = int(1e9)

water_q = deque([])

for i in range(r):
  board.append(list(input()))
  for j in range(c):
    if board[i][j] == "D":
      end_x, end_y = i, j
    elif board[i][j] == "S":
      start_x, start_y = i, j
    elif board[i][j] == "*":
      water_q.append((i, j))

visited_w = [[INF] * c for _ in range(r)]
visited = [[-1] * c for _ in range(r)]

# 물이 차는 최소 시간 구하기 (visited_x)
for x, y in water_q:
  visited_w[x][y] = 0

while water_q:
  x, y = water_q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<r and 0<=ny<c and visited_w[nx][ny] == INF and board[nx][ny] == ".":
      visited_w[nx][ny] = visited_w[x][y] + 1
      water_q.append((nx, ny))

q = deque([(start_x, start_y)])
visited[start_x][start_y] = 0
while q:
  x, y = q.popleft()

  if x == end_x and y == end_y:
    print(visited[x][y])
    exit()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<r and 0<=ny<c and board[nx][ny] != 'X' and visited[nx][ny] == -1 and visited[x][y] + 1 < visited_w[nx][ny]:
      q.append((nx, ny))
      visited[nx][ny] = visited[x][y] + 1

print("KAKTUS")