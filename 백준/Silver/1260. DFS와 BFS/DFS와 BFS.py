import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())  # 정점의 갯수, 간선의 갯수, 시작지점
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(n+1):
  graph[i].sort()

def dfs(v):
  visited[v] = True
  print(v, end=' ')

  for c in graph[v]:
    if not visited[c]:
      dfs(c)

def bfs(v):
  q = deque([v])
  visited[v] = True

  while q:
    v = q.popleft()
    print(v, end=' ')

    for c in graph[v]:
      if not visited[c]:
        q.append(c)
        visited[c] = True

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)