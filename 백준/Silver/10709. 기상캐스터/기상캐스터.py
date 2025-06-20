from collections import deque

h, w = map(int, input().split())
board = []
new_board = [[-1] * w for _ in range(h)]
clouds = deque()

for i in range(h):
  board.append(list(input()))
  for j in range(w):
    if board[i][j] == "c":
      new_board[i][j] = 0   # 처음부터 구역 (i, j)에 구름이 떠있는 경우 --> 0
      clouds.append((i, j))

while clouds:
  i, j = clouds.popleft()
  nj = j + 1

  if 0<=i<h and 0<=nj<w and new_board[i][nj] == -1:
    new_board[i][nj] = new_board[i][j] + 1
    clouds.append((i, nj))

for i in range(h):
  for j in range(w):
    print(new_board[i][j], end=" ")
  print()