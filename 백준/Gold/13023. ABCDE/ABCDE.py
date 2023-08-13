from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

def dfs(i, depth):
  if depth == 5:
    print(1)
    exit(0)

  for v in graph[i]:
    if not visited[v]:
      visited[v] = True
      dfs(v, depth+1)
      visited[v] = False


for i in range(n):
  dfs(i, 0)

print(0)