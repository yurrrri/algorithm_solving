import sys

n = int(sys.stdin.readline().rstrip()) #컴퓨터의 수
m = int(sys.stdin.readline().rstrip()) #컴퓨터 쌍
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(v):
  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

dfs(1)
print(visited.count(True)-1)