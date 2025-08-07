from collections import deque
from itertools import permutations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
  q = deque([(start_x, start_y)])
  visited[start_x][start_y] = 0

  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<h and 0<=ny<w and board[nx][ny] != "x" and visited[nx][ny] == -1:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  board = []
  robot_x, robot_y = 0, 0
  dirties = []
  for i in range(h):
    board.append(list(input()))
    for j in range(w):
      if board[i][j] == "o":
        robot_x, robot_y = i, j
      if board[i][j] == "*":
        dirties.append((i, j))

  # 1) 로봇과 각 먼지사이의 최단 거리 계산
  visited = [[-1] * w for _ in range(h)]
  bfs(robot_x, robot_y)
  robot_to_dust_destinations = [0] * len(dirties)  # 이후 첫번째로 방문할 먼지를 순열로 만들기 위해 사용할 로봇과 먼지 사이의 최단거리 배열
  flag = False
  
  for i, (x, y) in enumerate(dirties):
    if visited[x][y] == -1:
      flag = True
      break
    else:         # 로봇-먼지사이의 최단거리 배열을 최단거리로 갱신
      robot_to_dust_destinations[i] = visited[x][y]
      
  if flag:     # 방문할 수 없는 더러운 칸이 존재하므로 -1 출력 후 종료
    print(-1)
    continue

  # 2) 먼지와 먼지 사이의 최단거리 계산
  dist = [[0] * len(dirties) for _ in range(len(dirties))]
  for i in range(len(dirties)):
    visited = [[-1] * w for _ in range(h)]
    bfs(dirties[i][0], dirties[i][1])
    
    for j in range(len(dirties)):
      if i == j:
        continue

      if not dist[i][j] or not dist[j][i]:
        dist[i][j] = visited[dirties[j][0]][dirties[j][1]]
        dist[j][i] = dist[i][j]

  # 3) 순열을 통해 방문할 먼지 순서들을 정하여 이동 횟수의 최소값 갱신
  answer = int(1e9)
  for perm in permutations(range(len(dirties))):
    start = perm[0]
    _sum = robot_to_dust_destinations[start]
    for i in range(1, len(perm)):
      end = perm[i]
      _sum += dist[start][end]
      start = end

    answer = min(answer, _sum)

  print(answer)