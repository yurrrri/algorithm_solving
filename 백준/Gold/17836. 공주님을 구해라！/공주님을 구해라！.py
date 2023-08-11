from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())   # 제한 시간 t
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
	board.append(list(map(int, input().rstrip().split())))

# t안에 도착 못하는 조건: gram과 gram 안거치고 간 경로중 최소값이 t보다 크거나, 공주님한테 도착할 수 없을 때

def bfs():
	q = deque([(0, 0)])
	visited[0][0] = 1
	usedGramTime = 10001

	while q:
		x, y = q.popleft()

		if x == n-1 and y == m-1:
			return min(usedGramTime, visited[n-1][m-1]-1)

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
				if board[nx][ny] == 0:
					visited[nx][ny] = visited[x][y] + 1
					q.append((nx, ny))
				elif board[nx][ny] == 2: #그람이 있으면
					usedGramTime = visited[x][y] + n-nx-1 + m-ny-1
					visited[nx][ny] = usedGramTime

	return usedGramTime

result = bfs()
if result > t:
	print("Fail")
else:
	print(result)