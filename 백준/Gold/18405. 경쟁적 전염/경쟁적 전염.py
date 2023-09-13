from collections import deque

n, k = map(int, input().split())   # k 이하의 자연수로만 바이러스 번호가 이루어져있음
viruses = []
board = []
for i in range(n):
  read = list(map(int, input().split()))
  board.append(read)
  for j in range(n):
    if board[i][j] != 0:
      viruses.append((board[i][j], 0, i, j))

s, x, y = map(int, input().split())  # s초 뒤에 x-1, y-1 위치에 있는 바이러스 종류를 출력하면됨
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

viruses.sort()

def bfs():
  q = deque(viruses)

  while q:
    virus, cnt, x, y = q.popleft()

    if cnt == s:
      break
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
        board[nx][ny] = virus
        q.append((virus, cnt+1, nx, ny))

bfs()
print(board[x-1][y-1])