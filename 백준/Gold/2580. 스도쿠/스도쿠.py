board = []
zeroCoord = []

for i in range(9):
  board.append(list(map(int, input().split())))
  for j in range(9):
    if board[i][j] == 0:
      zeroCoord.append((i, j))

def isValid(num, x, y):
  if num in board[x]:     # 가로
    return False
  for i in range(9):      # 세로
    if board[i][y] == num:
      return False
  start = (x // 3) * 3
  end = (y // 3) * 3

  for i in range(start, start+3):       # 3x3 박스 안
    for j in range(end, end+3):
      if board[i][j] == num:
        return False

  return True

def backtracking(depth):
  if depth == len(zeroCoord):
    for i in range(9):
      for j in range(9):
        print(board[i][j], end=" ")
      print()
    exit()

  x, y = zeroCoord[depth]

  for i in range(1, 10):
    if isValid(i, x, y):
      board[x][y] = i
      backtracking(depth + 1)
      board[x][y] = 0

backtracking(0)