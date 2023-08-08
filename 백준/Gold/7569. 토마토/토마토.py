from collections import deque
import sys

input = sys.stdin.readline
m, n, h = map(int, input().rstrip().split())
#h: 높이 (세로로 몇층 쌓이는지)
q = deque()

board = []
for _ in range(h):
	temp = []
	for _ in range(n):
		temp.append(list(map(int, input().rstrip().split())))
	board.append(temp)

# 익은 토마토에서부터 시작해야하므로 익은 토마토 위치 받고 시작하기
for k in range(h):
	for i in range(n):
		for j in range(m):
			if board[k][i][j] == 1:
				q.append((k, i, j))

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

answer = []
visited = [[[False] * m]*n for _ in range(h)]

def bfs():
	while q:
		z, x, y = q.popleft()

		for i in range(6):
			nx = x + dx[i]
			ny = y + dy[i]
			nz = z + dz[i]

			if not (0<=nz<h and 0<=nx<n and 0<=ny<m):
				continue
			
			if board[nz][nx][ny] == 0:
				board[nz][nx][ny] = board[z][x][y] + 1
				q.append((nz, nx, ny))

bfs()
answer = 0

for k in range(h):
	for i in range(n):
		for j in range(m):
			if board[k][i][j] == 0:
				print(-1)
				exit(0)
			answer = max(answer, board[k][i][j])

print(answer-1)