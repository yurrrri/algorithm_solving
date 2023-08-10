from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
	x, y = map(int, input().rstrip().split())
	graph[x].append(y)
	graph[y].append(x)

answer = [0] * (n+1)
visited = [False] * (n+1)

def bfs():
	q = deque([1])
	visited[1] = True

	while q:
		v = q.popleft()
 
		for i in graph[v]:
			if not visited[i]:
				q.append(i)
				visited[i] = True
				
				answer[i] = v

bfs()

print('\n'.join(list(map(str, answer[2:]))))