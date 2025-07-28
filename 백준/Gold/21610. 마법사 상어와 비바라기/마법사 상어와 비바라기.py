n, m = map(int, input().split())
A = []       # A[r][c]: 바구니에 저장되어 있는 물의 양
for _ in range(n):
  A.append(list(map(int, input().split())))
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [[0] * n for _ in range(n)]

# 비바라기 시전
clouds[n-1][0] = 1
clouds[n-1][1] = 1
clouds[n-2][0] = 1
clouds[n-2][1] = 1

for _ in range(m):
  d, s = map(int, input().split())
  cloud_pos = []

  # 모든 구름이 d 방향으로 s칸 이동한다.
  for i in range(n):
    for j in range(n):
      if clouds[i][j] == 1:
        clouds[i][j] = 0
        
        ni = (i + dx[d] * s + n) % n
        nj = (j + dy[d] * s + n) % n

        cloud_pos.append((ni, nj))
    
  # 구름이 있는 칸의 바구니에 저장된 물의 양이 증가한다.
  for x, y in cloud_pos:
    A[x][y] += 1

  # 물복사 버그 마법 시전
  for x, y in cloud_pos:
    count = 0
    for i in range(2, 9, 2):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n and A[nx][ny] != 0:
        count += 1
    A[x][y] += count

  for i in range(n):
    for j in range(n):
      if A[i][j] >= 2 and (i, j) not in cloud_pos:
        clouds[i][j] = 1
        A[i][j] -= 2

answer = 0
for i in range(n):
  for j in range(n):
    answer += A[i][j]

print(answer)