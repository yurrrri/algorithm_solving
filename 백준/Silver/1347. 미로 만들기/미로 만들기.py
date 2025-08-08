n = int(input())
word = list(input())
x, y = 100, 100
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
min_x, max_x, min_y, max_y = 100, 100, 100, 100
board = [["#"] * 200 for _ in range(200)]
board[x][y] = "."

for w in word:
  if w == "L":
    d = (d + 1)%4
  elif w == "R":
    d = (d - 1)%4
  else:
    x += dx[d]
    y += dy[d]
    board[x][y] = "."
    
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        print(board[i][j], end='')
    print()