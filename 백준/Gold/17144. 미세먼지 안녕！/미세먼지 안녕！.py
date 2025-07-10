answer = 0
dx = [0, 1, 0, -1]  # 동, 남, 서, 북 순서
dy = [1, 0, -1, 0]

r, c, t = map(int, input().split())
machine = []
board = []
for i in range(r):
  board.append(list(map(int, input().split())))
  for j in range(c):
    if board[i][j] == -1:
      machine.append((i, j))

def spread():
  temp = [[0] * c for _ in range(r)]
  
  for x in range(r):
    for y in range(c):
      if board[x][y] > 0:   # 미세먼지가 있는곳
        count = 0    # 확산된 갯수
        amount = board[x][y] // 5
        for dir in range(4):
          nx = x + dx[dir]
          ny = y + dy[dir]

          # 칸이 없거나 (경계를 벗어나거나), 인접한 방향에 공기청정기가 있다면 확산이 일어나지 않는다.
          if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
            temp[nx][ny] += amount
            count += 1

        board[x][y] -= amount * count
        # 먼저 원래 미세먼지의 값을 업데이트해도 이후 미세먼지가 있는 곳에 영향을 주지 않는다. (최대 퍼질 수 있는 곳이 4곳이기 때문이기 때문에, board[x][y]가 0이 될 수 없음)

  for i in range(r):
    for j in range(c):
      board[i][j] += temp[i][j]
  
def purifying():
  # 위쪽
  # 동쪽부터시작하니 d=0
  d = 0
  before = 0  # 바람으로 밀어내기 전에 이전값을 저장할 변수, 공기청정기에서부터 밀어내니까 처음에는 0임
  #공기청정기 시작부분 다음칸부터 시작
  x, y = machine[0][0],machine[0][1]+1
  
  while True:
    # 공기청정기를 만나면 멈춤
    if x == machine[0][0] and y == machine[0][1]:
      break
      
    nx = x+dx[d]
    ny = y+dy[d]

    # 그 다음 위치가 바람이 벽을만나면 방향을 꺾음
    if nx == r or ny == c or nx == -1 or ny == -1:
      d -= 1
      continue
    
    board[x][y], before = before, board[x][y]   # 바람으로 밀어내고 (교환하고)
    x,y = nx,ny   # 방향 갱신

  # 아래쪽
  d=0
  before=0
  
  x,y = machine[1][0],machine[1][1]+1
  
  while True:
    if x == machine[1][0] and y ==machine[1][1]:
      break
      
    nx = x+dx[d]
    ny = y+dy[d]

    #바람이 벽을만나면 방향을 꺾음
    if nx == r or ny == c or nx == -1 or ny == -1:
      d += 1
      continue
    board[x][y],before = before,board[x][y]
    x,y=nx,ny
            
for _ in range(t):    # t초만큼 반복
  spread()
  purifying()

for i in range(r):
  for j in range(c):
    if board[i][j] > 0:
      answer += board[i][j]
      
print(answer)