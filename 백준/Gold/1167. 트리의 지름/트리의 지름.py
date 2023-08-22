from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
first = 0

for _ in range(n):
  read = list(map(int, input().rstrip().split()))
  for idx in range(1, len(read)-2, 2):
    graph[read[0]].append((read[idx], read[idx+1]))

answer = 0
def bfs(start, n):
  visited = [0] * n
  visited[start] = 1
  q = deque([start])
  maxValue = (0, 0) # 정점, 거리

  while q:
    node = q.popleft()

    for n, d in graph[node]:
      if not visited[n]:
        visited[n] = visited[node] + d
        q.append(n)
        if visited[n] > maxValue[1]:
          maxValue = (n, visited[n])

  return maxValue

node, dist = bfs(1, n+1)
node, dist = bfs(node, n+1)

print(dist-1)