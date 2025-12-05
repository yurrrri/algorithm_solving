from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input())))

def bfs():
  visited = [[-1] * m for _ in range(n)]    
  # 방문 여부와 검정색을 흰색으로 바꾼 갯수를 저장할 nxn 배열
  q = deque([(0, 0)])
  visited[0][0] = 0

  while q:
    x, y = q.popleft()

    # 끝방까지 도달할 수 있음
    if x == n-1 and y == m-1:
      return visited[x][y]
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
        if board[nx][ny] == 0:
            q.appendleft((nx, ny))
            visited[nx][ny] = visited[x][y]
        else:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(bfs())