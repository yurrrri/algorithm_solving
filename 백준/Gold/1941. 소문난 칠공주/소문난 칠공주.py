from collections import deque
import copy

board = []
for _ in range(5):
  board.append(list(input()))
visited = [[False] * 5 for _ in range(5)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtracking(num, start):   # 25개의 좌표 중 여학생 7명의 좌표를 고르는 백트래킹 함수
  global answer
  
  if num == 7:    # 7명을 다 뽑았으면
    if bfs():     # 7명의 학생들이 모두 인접해있는지, 이다솜파 여학생이 4명 이상인지를 판단한다.
      answer += 1
    return

  for i in range(start, 25):
      visited[i//5][i%5] = True
      backtracking(num+1, i+1)   # 중복되지 않게 뽑기 위해 i+1
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
        # BFS의 시작점을 정하기 위해, 기존 visited[i][j] = True, 즉 여학생의 후보지 중 하나를 시작점으로 고른다.

  q = deque([(start_x, start_y)])
  while q:
    x, y = q.popleft()

    for i in range(4):    # 상하좌우 인접한 칸들 대상으로 탐색
      nx = x + dx[i]
      ny = y + dy[i]

      if not (0<=nx<5 and 0<=ny<5):
        continue

      # 기존 7명의 여학생 중 하나의 좌표에 해당하는 경우 탐색 수행
      if visited[nx][ny] and not visited2[nx][ny]:
        visited2[nx][ny] = True
        total += 1
        q.append((nx, ny))
        if board[nx][ny] == "S":
          som += 1

  # 인접한 칸들을 대상으로 탐색을 진행했을 때, 기존 7명의 여학생 좌표가 탐색 가능하며 (즉 7명의 여학생들이 서로 인접해있음)
  # 이다솜파의 학생이 적어도 4명이상 포함되어있다면 return True
  if total == 7 and som >= 4:
    return True
  else:
    return False

backtracking(0, 0)
print(answer)