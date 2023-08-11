from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
visited = [False] * 100001

def bfs():
	global visited
	
	q = deque([(n, 0)])

	while q:
		x, dist = q.popleft()

		if x == k:
			print(dist)
			break

		if 0<=2*x<=100_000 and not visited[2*x]:
			q.appendleft((2*x, dist))
			visited[2*x] = True

		for nx in [x-1, x+1]:
			if 0<=nx<=100_000 and not visited[nx]:
				q.append((nx, dist+1))
				visited[nx] = True

bfs()