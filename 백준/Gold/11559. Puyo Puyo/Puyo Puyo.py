board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
coord = []
answer = 0

for i in range(12):
  board.append(list(input()))

def down():
  for y in range(6):
    for i in range(10, -1, -1):
      for x in range(11, i, -1):
        if board[x][y] == "." and board[i][y] != ".":
          board[x][y] = board[i][y]
          board[i][y] = "."


def dfs(x, y, color):
  visited[x][y] = True
  temp.append((x, y))

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and board[nx][ny] == color:
       dfs(nx, ny, color)

while True:
  flag = True    # 반복문을 멈출 flag 변수
  visited = [[False] * 6 for _ in range(12)]

  for i in range(12):
    for j in range(6):
      if board[i][j] != "." and not visited[i][j]:   # 새롭게 영역을 탐색할 뿌요일 경우, 그래프탐색 실행
        temp = []
        dfs(i, j, board[i][j])

        if len(temp) >= 4:
          flag = False
          for i, j in temp:
            board[i][j] = "."

  if flag:   # 더이상 터뜨릴 뿌요가 없다면
    break

  down()
  answer += 1

print(answer)