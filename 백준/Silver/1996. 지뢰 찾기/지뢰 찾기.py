n = int(input())
map = []
for _ in range(n):
  map.append(list(input()))
answer = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for x in range(n):
  for y in range(n):
    if map[x][y] != ".":
      answer[x][y] = -1  # 이후 * 표시
      
      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and answer[nx][ny] != -1:
          answer[nx][ny] += int(map[x][y])

for x in range(n):
  for y in range(n):
    if answer[x][y] == -1:
      print("*", end = '')
    elif answer[x][y] >= 10:
      print("M", end = '')
    else:
      print(answer[x][y], end = '')
  print()