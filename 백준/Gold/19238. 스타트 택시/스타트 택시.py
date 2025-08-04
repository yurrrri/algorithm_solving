from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, e = map(int, input().split())   # e: c초기 연료의 양, 연료는 무한히 담을 수 있음
board = []
for i in range(n):    # 0은 빈칸, 1은 벽
  board.append(list(map(int, input().split())))
customers = {}   # 각 승객의 번호와 현재 위치, 목적지 위치를 저장할 딕셔너리
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1   # 택시의 시작 위치
for i in range(m):
  start_x, start_y, end_x, end_y = map(int, input().split())
  customers[i] = [start_x-1, start_y-1, end_x-1, end_y-1]

def bfs(from_x, from_y):   # 최단경로 -> BFS
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

  for k, v in customers.items():
    if visited[v[0]][v[1]] == -1:   # 탐색을 진행하였는데 손님의 위치 중 1개가 -1이라는 것은 손님을 태우러가기 어렵다는 의미이므로, -1을 출력하고 종료한다.
      print(-1)
      exit()

  # arr: 현재 위치에서 최단거리가 가장 짧고, 행 번호가 가장 작고, 열 번호가 가장 작은 순서대로 정렬하여 손님을 태우러 가기 위해 사용하는 배열
  arr = []
  for k, v in customers.items():
    arr.append((k, v[0], v[1], visited[v[0]][v[1]]))
  arr.sort(key=lambda x:(x[3], x[1], x[2]))

  # 손님을 고름
  customer = arr[0][0]

  # 손님을 태우러가다가 기름 다 떨어지면 -1 반환
  if e - arr[0][3] < 0:
    print(-1)
    exit()

  # 손님을 태우러 감
  customer_start_x, customer_start_y = customers[customer][0], customers[customer][1]
  taxi_x, taxi_y = customer_start_x, customer_start_y
  e -= visited[taxi_x][taxi_y]  # 연료 소모

  # 목적지로 이동하기 위해 현재 손님 위치에서 목적지까지의 최단거리 구하기
  visited = [[-1] * n for _ in range(n)]
  bfs(customer_start_x, customer_start_y)

  # 만약에 목적지까지 이동하는 도중에 연료가 떨어지면 -1 출력하고 종료
  customer_to_x, customer_to_y = customers[customer][2], customers[customer][3]
  # 목적지까지 이동하는 도중에 연료 떨어지면 -1 출력 후 종료
  if e - visited[customer_to_x][customer_to_y] < 0:
    print(-1)
    exit()
    
  # 연료 소모 하여 도착
  taxi_x, taxi_y = customer_to_x, customer_to_y
  e -= visited[customer_to_x][customer_to_y]

  # 도착에 성공했으므로 소모한 연료 양의 2배 충전됨
  e += visited[customer_to_x][customer_to_y] * 2

  # 손님 태웠으니까 태워야할 손님 딕셔너리에서 제거함
  del customers[customer]
  
print(e)