from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]  # 인접한 한칸 혹은 대각선 방향, 현재 위치에 서있을 수 있음

# board에서 벽 아래로 이동하는 함수 하나
# DFS 혹은 BFS -> 이때 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없음

board = []
bricks = []
for i in range(8):
  temp = list(input())
  board.append(temp)
  for j in range(8):
    if board[i][j] == "#":
      bricks.append((i, j))

def move_wall(board):
    new = [['.'] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                if i + 1 < 8:
                    new[i+1][j] = '#'
    return new

def bfs():
  q = deque([(7, 0)])

  while q:
    visited = [[False] * 8 for _ in range(8)]
    
    for _ in range(len(q)):
      x, y = q.popleft()
      if board[x][y] == '#':
          continue
      if x == 0 and y == 7:
        return 1

      for i in range(9):
          nx = x + dx[i]
          ny = y + dy[i]

          if 0<=nx<8 and 0<=ny<8 and not visited[nx][ny]:
              if board[nx][ny] == '.':
                  q.append((nx, ny))
                  visited[nx][ny] = True

    board[:] = move_wall(board)

  return 0

print(bfs())