from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
visited = [0] * 100001

def bfs():
	global board
	global visited
	
	q = deque([n])
	visited[n] = 0

	while q:
		x = q.popleft()

		if x == k:
			print(visited[k])
			break

		for nx in [x-1, x+1, 2*x]:
			if 0<=nx<=100_000 and not visited[nx]:
				q.append(nx)
				visited[nx] = visited[x] + 1

bfs()