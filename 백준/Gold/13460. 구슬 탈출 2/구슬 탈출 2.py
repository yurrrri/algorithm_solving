from collections import deque

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
  board.append(list(input()))
  for j in range(m):
    if board[i][j] == "R":
      red_x, red_y = i, j
    if board[i][j] == "B":
      blue_x, blue_y = i, j

# BFS 사전작업
visited[red_x][red_y][blue_x][blue_y] = True
q = deque([(red_x, red_y, blue_x, blue_y, 1)])

# 구슬이 움직이는 동작 표현
def move(x, y, dx, dy):
    count = 0	# 이동한 칸 수
    # 이동한 칸 수를 알게되면 어느 구슬이 더 많이 움직인지 알 수 있음

    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        # 다음에 이동할 좌표가 벽이 아니거나 현재 좌표가 구멍이 아닐 경우에
        x += dx
        y += dy
        # 현재 좌표를 한칸 전진하고
        count += 1
        # 한칸 전진했으므로 +1을 해준다

    return x, y, count
  
while q:
    red_x, red_y, blue_x, blue_y, n = q.popleft()

    # 구슬이 움직이는 횟수는 10번 이하여야 함
    if n > 10:
        break

    # 네 가지 기울이기 동작 시행
    for i in range(4):
        red_nx, red_ny, r_count = move(red_x, red_y, dx[i], dy[i])	# 빨간 구슬 이동
        blue_nx, blue_ny, b_count = move(blue_x, blue_y, dx[i], dy[i]) # 파란 구슬 이동

        # 파란구슬이 구멍에 도착했다면 실패
        if board[blue_nx][blue_ny] == 'O':
            continue

        # 빨간공과 파란공이 같은 위치에서 멈추면 (겹치게된다면)
        if red_nx == blue_nx and red_ny == blue_ny:
            # 움직임이 많은 구슬이 다른 구슬보다 한칸 적어야함
            if r_count > b_count:
              red_ny -= dy[i]
              red_nx -= dx[i]
            else:
              blue_ny -= dy[i]
              blue_nx -= dx[i]

        # 빨간구슬이 구멍에 도착했다면 성공
        if board[red_nx][red_ny] == 'O':
            print(n)
            exit(0)

        # 1회의 구슬 이동을 마치고 도달한 좌표값이 예전에 방문했던 적이 없다면 새로 큐에 추가
        if not visited[red_nx][red_ny][blue_nx][blue_ny]:
            visited[red_nx][red_ny][blue_nx][blue_ny] = True
            q.append((red_nx, red_ny, blue_nx, blue_ny, n+1))

print(-1)