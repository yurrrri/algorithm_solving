from collections import deque

# 검은 방은 들어갈 수 없고, 서로 인접한 두 개의 흰방 사이에는 문에 있어서 지나다닐 수 있다 -> 인접하게 이동할 수 있는 offset 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input())))

def bfs():
  visited = [[-1] * n for _ in range(n)]    
  # 방문 여부와 검정색을 흰색으로 바꾼 갯수를 저장할 nxn 배열
  q = deque([(0, 0)])
  visited[0][0] = 0

  while q:
    x, y = q.popleft()

    # 끝방까지 도달할 수 있음
    if x == n-1 and y == n-1:
      return visited[x][y]
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
        if board[nx][ny] == 1:   # 흰색 방인 경우 가중치 0 -> appendleft
            q.appendleft((nx, ny))
            visited[nx][ny] = visited[x][y]
        else:    # 검은색 방인 경우 부숴야 하니까 가중치 1 -> append, 흰색으로 바꾸는 경우의 수 갱신
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(bfs())