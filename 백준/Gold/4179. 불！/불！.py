from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
board = []
fire_q = deque([])
fire_visited = [[0] * c for _ in range(r)]
q = deque([])
visited = [[0] * c for _ in range(r)]

for i in range(r):
  board.append(input())
  for j in range(c):
    if board[i][j] == "J":
      q.append((i, j))
      visited[i][j] = 1
    elif board[i][j] == "F":
      fire_q.append((i, j))
      fire_visited[i][j] = 1

answer = 0

def fire_bfs():
  while fire_q:
    x, y = fire_q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<r and 0<=ny<c and board[nx][ny] != "#" and not fire_visited[nx][ny]:
        fire_visited[nx][ny] = fire_visited[x][y] + 1
        fire_q.append((nx, ny))

def bfs():
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<r and 0<=ny<c and board[nx][ny] == "." and not visited[nx][ny]:
        if (not fire_visited[nx][ny] or fire_visited[nx][ny] > visited[x][y] + 1):
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))
        
      elif not(0<=nx<r and 0<=ny<c):  # 범위를 벗어나면 탈출할 수 있다는 의미이므로 거리 출력하고 break
        return visited[x][y]

  return -1

fire_bfs()
result = bfs()
if result == -1:
  print("IMPOSSIBLE")
else:
  print(result)