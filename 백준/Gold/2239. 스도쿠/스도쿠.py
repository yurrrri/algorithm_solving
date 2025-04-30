import sys
input = sys.stdin.readline

board = []

for _ in range(9):
  board.append(list(map(int, str(input().rstrip()))))

def valid_in_col(col, num):
  for i in range(9):
    if board[i][col] == num:
      return False
  return True

def valid_in_row(row, num):
  for i in range(9):
    if board[row][i] == num:
      return False
  return True

def valid_in_box(row, col, num):
  area_row = (row // 3) * 3
  area_col = (col // 3) * 3
  for i in range(area_row, area_row + 3):
    for j in range(area_col, area_col + 3):
      if board[i][j] == num:
        return False

  return True

def find_zero():
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        return i, j

  return -1, -1

def backtracking():
  x, y = find_zero()
  if (x, y) == (-1, -1):
    for i in range(9):
      for j in range(9):
        print(board[i][j], end = "")
      print()

    sys.exit(0)

  for i in range(1, 10):
    if valid_in_col(y, i) and valid_in_row(x, i) and valid_in_box(x, y, i):
      board[x][y] = i
      backtracking()
      board[x][y] = 0

backtracking()