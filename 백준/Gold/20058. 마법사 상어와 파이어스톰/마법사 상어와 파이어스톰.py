from collections import deque

n, q = map(int, input().split())   # q번 시전
que = []    # 마법사 상어가 시전한 단계
grid = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(2**n):
  grid.append(list(map(int, input().split())))
que = list(map(int, input().split()))

def rotate_subgrid(grid, x, y, l):
  size = 2 ** l
  new_grid = [[0] * size for _ in range(size)]
  for i in range(size):
      for j in range(size):
          new_grid[j][size - 1 - i] = grid[x + i][y + j]
  for i in range(size):
      for j in range(size):
          grid[x + i][y + j] = new_grid[i][j]

def rotate_all(grid, l):
  n = len(grid)
  step = 2 ** l
  for i in range(0, n, step):
    for j in range(0, n, step):
        rotate_subgrid(grid, i, j, l)

def judge(x, y):    # 얼음이 있는 칸 3개 혹은 그 이상과 인접해있지 않은 칸을 판단하기 위한 함수
  count = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<2**n and 0<=ny<2**n and grid[nx][ny] > 0:
      count += 1

  if count >= 3:
    return True
  else:
    return False

visited = [[False] * 2**n for _ in range(2**n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 2**n and 0 <= ny < 2**n:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

def count_ice():
  count = 0
  
  for i in range(2**n):
    for j in range(2**n):
      count += grid[i][j]

  return count

for l in que:
  rotate_all(grid, l)
  to_reduce_ice = []

  for i in range(2**n):
    for j in range(2**n):
      if grid[i][j] > 0 and not judge(i, j):
        to_reduce_ice.append((i, j))

  for x, y in to_reduce_ice:
    grid[x][y] -= 1
  
answer1 = count_ice()
print(answer1)

answer2 = 0
for i in range(2**n):
  for j in range(2**n):
    if grid[i][j] > 0 and not visited[i][j]:
      answer2 = max(answer2, bfs(i, j))
print(answer2)