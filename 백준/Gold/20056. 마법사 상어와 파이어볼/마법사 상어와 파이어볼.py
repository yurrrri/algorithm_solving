import copy

N, M, K = map(int, input().split())  # n: 격자크기 m: 파이어볼 갯수, k: 명령한 횟수
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
board = [[[] for _ in range(N)] for _ in range(N)]
infos = []
answer = 0

for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  infos.append([r-1, c-1, m, d, s])
  board[r-1][c-1].append([m, d, s])

def move():
  for x, y, m, d, s in infos:
    nx = (x + dx[d] * s) % N
    ny = (y + dy[d] * s) % N
    board[nx][ny].append([m, d, s])
    board[x][y].remove([m, d, s])

for _ in range(K):
  move()

  for x in range(N):
    for y in range(N):
      if len(board[x][y]) >= 2:
        _len = len(board[x][y])
        m = 0   # 질량의 합
        s = 0   # 속력의 합
        even_count, odd_count = 0, 0
        for M, D, S in board[x][y]:
          m += M
          s += S
          if D%2 == 0:
            even_count += 1
          else:
            odd_count += 1

        m //= 5
        s //= _len
        if m > 0:
          if even_count == _len or odd_count == _len:
            board[x][y] = [[m, 0, s], [m, 2, s], [m, 4, s], [m, 6, s]]
          else:
            board[x][y] = [[m, 1, s], [m, 3, s], [m, 5, s], [m, 7, s]]
        else:
          board[x][y] = []

  infos = []
  for x in range(N):
    for y in range(N):
      if board[x][y]:
        for m, d, s in board[x][y]:
          infos.append([x, y, m, d, s])

for x in range(N):
  for y in range(N):
    if board[x][y]:
      for m, _, _ in board[x][y]:
        answer += m

print(answer)