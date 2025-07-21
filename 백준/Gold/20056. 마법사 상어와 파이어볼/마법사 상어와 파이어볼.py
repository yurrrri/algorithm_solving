N, M, K = map(int, input().split())  # n: 격자크기 m: 파이어볼 갯수, k: 명령한 횟수
dx = [-1, -1, 0, 1, 1, 1, 0, -1]   # 사진의 0 ~ 8의 방향대로 이동할 offset 배열
dy = [0, 1, 1, 1, 0, -1, -1, -1]
board = [[[] for _ in range(N)] for _ in range(N)]
infos = []   # 파이어볼의 정보를 담을 배열
answer = 0

for _ in range(M):
  r, c, m, s, d = map(int, input().split())
  infos.append([r-1, c-1, m, d, s])

def move():
  while infos:
    x, y, m, d, s  = infos.pop()
    nx = (x + dx[d] * s) % N      # d의 방향대로 s만큼 이동
    ny = (y + dy[d] * s) % N      # N으로 나누는 이유는 1행과 1열은 각각 N행, N열과 연결되어있기 때문이다. 
    board[nx][ny].append([m, d, s])

for _ in range(K):    # K회 만큼 명령
  move()           # 파이어볼 움직이기

  for x in range(N):            # 파이어볼 나누는 과정
    for y in range(N):
      if len(board[x][y]) >= 2:    # 2개 이상의 파이어볼이 들어있을 경우,
        _len = len(board[x][y])
        m = 0   # 질량의 합
        s = 0   # 속력의 합
        even_count, odd_count = 0, 0
        while board[x][y]:
          M, D, S = board[x][y].pop()
          m += M
          s += S
          if D%2 == 0:
            even_count += 1
          else:
            odd_count += 1

        m //= 5
        s //= _len
        if m > 0:
          if even_count == _len or odd_count == _len:   # 모든 파이어볼의 방향이 짝수 혹은 홀수라면
            infos.extend([[x, y, m, 0, s], [x, y, m, 2, s], [x, y, m, 4, s], [x, y, m, 6, s]])
          else:
            infos.extend([[x, y, m, 1, s], [x, y, m, 3, s], [x, y, m, 5, s], [x, y, m, 7, s]])

      if len(board[x][y]) == 1:
        infos.append([x, y] + board[x][y].pop())

print(sum([f[2] for f in infos]))