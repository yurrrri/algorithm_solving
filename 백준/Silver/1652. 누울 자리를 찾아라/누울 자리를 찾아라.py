n = int(input())
board = []
for _ in range(n):
  board.append(input())
garo, sero = 0, 0

for i in range(n):
  count = 0
  for j in range(n):
    if board[i][j] == ".":
      count += 1
    if board[i][j] == "X":
      if count >= 2:
        garo += 1
      count = 0
      continue
    if j == n-1:
      if count >= 2:
        garo += 1

for i in range(n):
  count = 0
  for j in range(n):
    if board[j][i] == ".":
      count += 1
    if board[j][i] == "X":
      if count >= 2:
        sero += 1
      count = 0
      continue
    if j == n-1:
      if count >= 2:
        sero += 1

print(garo, sero)