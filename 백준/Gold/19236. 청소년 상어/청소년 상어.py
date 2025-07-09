import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]  # 1부터 8까지 차례대로 방향 offset 배열
answer = 0

fishes = []          # 입력받기
for _ in range(4):
  temp = list(map(int, input().split()))
  row = []
  for j in range(0, 8, 2):
    a, b = temp[j : j + 2]
    row.append([a, b - 1])   # 물고기 번호, 방향
  fishes.append(row)

def find_coord(board, num):    # 물고기 좌표 찾기
  for i in range(4):
    for j in range(4):
      if board[i][j][0] == num:
        return i, j

  return -1, -1   # 못찾은 경우

def moving_fishes(board, shark_x, shark_y):
  for i in range(1, 17):  # 번호가 작은 물고기부터 이동한다.
    x, y = find_coord(board, i)   # 물고기 좌표 찾기
    
    if x == -1 and y == -1:    # 이미 먹힌 물고기이므로, 다음 물고기의 이동 작업을 시작한다.
      continue
      
    dir = board[x][y][1]
      
    for j in range(8): 
      # 이동할 수 있는 칸을 찾을 때까지 45도 반시계 회전시킨다.
      nd = (dir + j) % 8
      nx = x + dx[nd]
      ny = y + dy[nd]

      # 이동할 수 없는 칸: 경계를 벗어나거나, 상어가 있거나
      if not (0<=nx<4 and 0<=ny<4): 
        continue

      if nx == shark_x and ny == shark_y:
        continue

      # 이동할 수 있는 칸이 있다면, 물고기와 방향 포함해서 같이 위치 바뀜
      board[x][y][1] = nd  # 이동할 수 있는 방향으로 갱신한 다음,
      board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
      break    # 이동할 수 있는 칸을 찾았으므로 break
      
def positions_shark_can_go(board, shark_x, shark_y, dir):
  positions = []
  
  for _ in range(3):   # 상어는 방향에 있는 칸으로 이동할 수 있고, 한번에 여러개의 칸을 이동할 수 있다.
    shark_x += dx[dir]
    shark_y += dy[dir]

    if 0<=shark_x<4 and 0<=shark_y<4 and board[shark_x][shark_y][0] != 0:        # 물고기가 없는 칸으로는 이동할 수 없다.
      positions.append((shark_x, shark_y))

  return positions

def dfs(x, y, board, total):
  global answer

  # 상태마다 board의 상태가 바뀌므로 복사 필요함
  copied = copy.deepcopy(board)
  
  total += copied[x][y][0]   # 물고기를 먹음
  copied[x][y][0] = 0        # 먹는 상태로 처리

  moving_fishes(copied, x, y)   # 물고기 움직임

  positions = positions_shark_can_go(copied, x, y, copied[x][y][1])

  if not positions:           # 더이상 이동할 수 없다면 answer 갱신하고 되돌아가기
    answer = max(answer, total)
    return

  for nx, ny in positions:   # 이동할 수 있는 모든 칸에 대해 탐색 진행
    dfs(nx, ny, copied, total)

# 0, 0에서부터 시작함
dfs(0, 0, fishes, 0)

print(answer)