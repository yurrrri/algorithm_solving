c, r = map(int, input().split())
k = int(input())

if k > c*r:
  print(0)
  exit()
  
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * r for _ in range(c)]

temp = 1
x, y = 0, 0
d = 0

while True:
  if temp == k:
    print(x+1, y+1)
    break

  visited[x][y] = True
  nx = x + dx[d]
  ny = y + dy[d]

  if 0<=nx<c and 0<=ny<r:
    if not visited[nx][ny]:
      x = nx
      y = ny
      temp += 1
    else:
      d = (d+1) % 4
  else:
    d = (d+1) % 4