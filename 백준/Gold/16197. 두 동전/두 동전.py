from collections import deque

n, m = map(int, input().split())   # 세로 크기: n, 가로 크기: m
board = []
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
temp = []

for i in range(n):
  read = list(input())
  board.append(read)
  for j in range(m):
    if board[i][j] == "o":
      temp.append((i, j))   # 동전은 항상 2개이며, 동시에 이동한다.
      
def bfs():
  q.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
  
  while q:
    x1, y1, x2, y2, c = q.popleft()  # 좌표, 버튼을 눌러야 하는 개수
    
    if c >= 10:   # 버튼을 10번보다 많이 눌러야 한다면 -1 출력
      return -1

    for i in range(4):
      nx1 = x1 + dx[i]
      ny1 = y1 + dy[i]
      nx2 = x2 + dx[i]
      ny2 = y2 + dy[i]

      if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m: # 두 동전 다 범위안에 있다면
        # 벽이라면
        if board[nx1][ny1] == "#":
            nx1, ny1 = x1, y1
        if board[nx2][ny2] == "#":
            nx2, ny2 = x2, y2
        q.append((nx1, ny1, nx2, ny2, c + 1))   # 동전은 이동할 지역이 벽이라면 이동하지 않음
      elif (0 <= nx1 < n and 0 <= ny1 < m) or (0<=nx2<n and 0<=ny2<m):  # 두 동전 중 하나라도 바닥에 떨어진다면 바로 버튼을 누른 횟수 return
        return c + 1

  return -1   # 두 동전을 모두 떨어뜨릴 수 없다면 -1 출력

print(bfs())