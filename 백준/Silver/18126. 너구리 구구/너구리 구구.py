import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

answer = 0

def dfs(v, cost):
  global answer
  visited[v] = True
  
  answer = max(answer, cost)

  for c, m in graph[v]:
    if not visited[c]:
      dfs(c, cost + m)

dfs(1, 0)
print(answer)