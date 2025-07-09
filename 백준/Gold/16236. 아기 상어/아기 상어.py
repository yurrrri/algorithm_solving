from collections import deque

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
x, y = 0, 0   # 아기상어의 위치
size = 2   # 가장 처음 아기 상어의 크기는 2이다.

for i in range(n):
  board.append(list(map(int, input().split())))
  for j in range(n):
    if board[i][j] == 9:   # 아기상어 위치 찾음
      x, y = i, j
      board[x][y] = 0

def bfs():
  q = deque([(x, y)])
  visited = [[-1] * n for _ in range(n)]
  visited[x][y] = 0

  while q:
    nx, ny = q.popleft()

    for i in range(4):
      mx = nx + dx[i]
      my = ny + dy[i]

      if 0<=mx<n and 0<=my<n and visited[mx][my] == -1 and board[mx][my] <= size:
        visited[mx][my] = visited[nx][ny] + 1
        q.append((mx, my))

  positions = []
  for i in range(n):
    for j in range(n):
      if 0 < board[i][j] < size and visited[i][j] != -1:
        positions.append((i, j, visited[i][j]))

  return positions

count = 0
while True:
  positions = bfs()
  
  if not positions:  # 먹을 수 있는 물고기가 없음
    break

  positions.sort(key=lambda x:(x[2], x[0], x[1]))
  nx, ny, dist = positions[0]
  
  count += 1
  board[nx][ny] = 0
  x, y = nx, ny
  answer += dist
  
  if count == size:
    size += 1
    count = 0

print(answer)