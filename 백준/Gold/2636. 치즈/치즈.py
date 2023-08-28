import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = []
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  board.append(list(map(int, input().rstrip().split())))

visited = [[False] * m for _ in range(n)]
ans = []

def bfs():
  q = deque([(0, 0)])
  visited[0][0] = True
  count = 0
  
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        visited[nx][ny] = True
        
        if board[nx][ny] == 1:
          board[nx][ny] = 0
          count += 1
        elif board[nx][ny] == 0:
          q.append((nx, ny))

  ans.append(count)
  
  return count

time = 0
count = -1
while True:
  visited = [[False] * m for _ in range(n)]
  count = bfs()
  if count == 0:
    print(time)
    print(ans[-2])
    break
  time += 1