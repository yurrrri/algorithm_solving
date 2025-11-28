from collections import deque
import copy

board = []
for _ in range(5):
  board.append(list(input()))
visited = [[False] * 5 for _ in range(5)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtracking(num, start):
  global answer
  
  if num == 7:
    if bfs():
      answer += 1
    return

  for i in range(start, 25):
      visited[i//5][i%5] = True
      backtracking(num + 1, i+1)
      visited[i//5][i%5] = False

def bfs():
  visited2 = [[False] * 5 for _ in range(5)]
  start_x = 0
  start_y = 0
  total, som = 0, 0
  
  for i in range(5):
    for j in range(5):
      if visited[i][j]:
        start_x, start_y = i, j

  q = deque([(start_x, start_y)])
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<5 and 0<=ny<5:
        if visited[nx][ny] and not visited2[nx][ny]:
          visited2[nx][ny] = True
          total += 1
          q.append((nx, ny))
          if board[nx][ny] == "S":
            som += 1

  if total == 7 and som >= 4:
    return True
  else:
    return False

backtracking(0, 0)
print(answer)