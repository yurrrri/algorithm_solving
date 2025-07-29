from itertools import combinations
from collections import deque
import sys

n, m = map(int, input().split())   # m개의 바이러스를 활성상태로 둘 수 있음
board = []    # nxn 인 연구소
viruses = []
zero_count = 0
for i in range(n):
  board.append(list(map(int, input().split())))
  for j in range(n):
    if board[i][j] == 2:
      viruses.append((i, j))
    if board[i][j] == 0:
      zero_count += 1

if zero_count == 0:
  print(0)
  exit()
      
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = sys.maxsize
answer = INF
combi = combinations(viruses, m)

def bfs():
  max_time = 0
  zero_count2 = 0
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
        if board[nx][ny] == 0:
          zero_count2 += 1
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
          max_time = max(visited[nx][ny], max_time)
        elif board[nx][ny] == 2:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1

  if zero_count == zero_count2:
    return max_time
  else:
    return INF

for c in combi:
  q = deque([])
  visited = [[-1] * n for _ in range(n)]
  for x, y in c:
    q.append((x, y))
    visited[x][y] = 0
  answer = min(answer, bfs())

if answer == INF:
  print(-1)
else:
  print(answer)