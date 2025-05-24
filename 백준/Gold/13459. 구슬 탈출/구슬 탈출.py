from collections import deque

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
  board.append(list(input()))
  for j in range(m):
    if board[i][j] == "R":
      a, b = i, j
    if board[i][j] == "B":
      c, d = i, j

def move(x, y, i):

  count = 0
  
  while board[x+dx[i]][y+dy[i]] != "#" and board[x][y] != "O":
    x += dx[i]
    y += dy[i]
    count += 1

  return x, y, count

q = deque([(a, b, c, d, 1)])
visited[a][b][c][d] = True

while q:
  red_x, red_y, blue_x, blue_y, n = q.popleft()

  if n > 10:
    break
    
  for i in range(4):
    red_nx, red_ny, red_count = move(red_x, red_y, i)
    blue_nx, blue_ny, blue_count = move(blue_x, blue_y, i)
        
    if board[blue_nx][blue_ny] == 'O':
      continue  # 실패

    if board[red_nx][red_ny] == 'O':
      print(1)
      exit(0)

    if red_nx == blue_nx and red_ny == blue_ny:
      if red_count > blue_count:
        red_nx -= dx[i]
        red_ny -= dy[i]
      else:
        blue_nx -= dx[i]
        blue_ny -= dy[i]

    if not visited[red_nx][red_ny][blue_nx][blue_ny]:
      q.append((red_nx, red_ny, blue_nx, blue_ny, n+1))
      visited[red_nx][red_ny][blue_nx][blue_ny] = True

print(0)