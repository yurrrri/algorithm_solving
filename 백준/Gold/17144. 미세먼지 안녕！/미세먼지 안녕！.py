answer = 0
dx = [0, 1, 0, -1]
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
    temp = [[0]*c for _ in range(r)]
    
    for x in range(r):
      for y in range(c):
        if board[x][y] > 0:
          amount = board[x][y] // 5
          count = 0
          for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
              temp[nx][ny] += amount
              count += 1
          board[x][y] -= amount * count

    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]

def purifying():
  upper, lower = machine[0][0], machine[1][0]

  # 위쪽: 반시계 방향
  for i in range(upper-1, 0, -1): board[i][0] = board[i-1][0]
  for i in range(c-1): board[0][i] = board[0][i+1]
  for i in range(upper): board[i][c-1] = board[i+1][c-1]
  for i in range(c-1, 1, -1): board[upper][i] = board[upper][i-1]
  board[upper][1] = 0

  # 아래쪽: 시계 방향
  for i in range(lower+1, r-1): board[i][0] = board[i+1][0]
  for i in range(c-1): board[r-1][i] = board[r-1][i+1]
  for i in range(r-1, lower, -1): board[i][c-1] = board[i-1][c-1]
  for i in range(c-1, 1, -1): board[lower][i] = board[lower][i-1]
  board[lower][1] = 0
            
for _ in range(t):    # t초만큼 반복
  spread()
  purifying()

for i in range(r):
  for j in range(c):
    if board[i][j] > 0:
      answer += board[i][j]
      
print(answer)