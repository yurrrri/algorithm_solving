from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
q = deque([])

for _ in range(n):
	board.append(list(map(int, input().rstrip().split())))

for i in range(n):
	for j in range(m):
		if board[i][j] == 1:
			q.append((i, j))

answer = 0

def bfs():
	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
				board[nx][ny] = board[x][y] + 1
				q.append((nx, ny))

bfs()
for i in range(n):
	for j in range(m):
		if board[i][j] == 0:
			print(-1)
			exit(0)
		answer = max(board[i][j], answer)

print(answer-1)