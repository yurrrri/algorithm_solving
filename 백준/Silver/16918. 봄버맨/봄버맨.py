r, c, n = map(int, input().split())   # rxc 직사각형, n초가 지난후의 격자판 상태 출력
board = []
bombs = []
for i in range(r):
  board.append(list(input()))
  for j in range(c):
    if board[i][j] == "O":
      bombs.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bang():
  for (x, y) in bombs:
    board[x][y] = "."
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<r and 0<=ny<c:
        board[nx][ny] = "."    # 인접한 곳에 폭탄이 있어도 파괴되므로 따로 폭탄 여부 안따져도 됨

for i in range(2, n+1):
  # 1. 폭탄 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
  if i % 2 == 0:
    board = [["O"] * c for _ in range(r)]
  else:  # 2. 3초 전에 설치된 폭탄이 모두 폭발한다.
    bang()
    bombs = []
    for i in range(r):
      for j in range(c):
        if board[i][j] == "O":
          bombs.append((i, j))

for i in range(r):
  print("".join(board[i]))