from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, e = map(int, input().split())   # e: c초기 연료의 양, 연료는 무한히 담을 수 있음
board = []
for i in range(n):    # 0은 빈칸, 1은 벽
  board.append(list(map(int, input().split())))
customers = {}
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1   # 택시의 시작 위치
for i in range(m):
  start_x, start_y, end_x, end_y = map(int, input().split())
  customers[i] = [start_x-1, start_y-1, end_x-1, end_y-1]

def bfs(from_x, from_y):
  visited[from_x][from_y] = 0
  q = deque([(from_x, from_y)])

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0 and visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

while customers:   # 모든 승객을 데려다줄때까지
  visited = [[-1] * n for _ in range(n)]
  bfs(taxi_x, taxi_y)

  for k, v in customers.items():   # 승객을 데리러 가는거 자체가 안됨
    if visited[v[0]][v[1]] == -1:
      print(-1)
      exit()

  # 현재 위치에서 최단거리가 가장 짧은 승객을 고르기 위한 배열
  arr = []
  for k, v in customers.items():
    arr.append((k, v[0], v[1], visited[v[0]][v[1]]))
  arr.sort(key=lambda x:(x[3], x[1], x[2]))

  customer = arr[0][0]

  if e - arr[0][3] < 0:   # 손님을 태우러가다가 기름 다 떨어지면 -1 반환
    print(-1)
    exit()

  taxi_x, taxi_y = customers[customer][0], customers[customer][1]
  e -= visited[taxi_x][taxi_y]
  
  visited = [[-1] * n for _ in range(n)]
  bfs(customers[customer][0], customers[customer][1])

  if e - visited[customers[customer][2]][customers[customer][3]] < 0:
    print(-1)
    exit()
    
  e -= visited[customers[customer][2]][customers[customer][3]]
  e += visited[customers[customer][2]][customers[customer][3]] * 2
  taxi_x, taxi_y = customers[customer][2], customers[customer][3]
  del customers[customer]
  
print(e)