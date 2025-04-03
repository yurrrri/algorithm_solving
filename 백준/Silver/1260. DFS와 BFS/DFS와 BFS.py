import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n+1)

def dfs(v):
  visited[v] = True
  print(v, end=' ')

  graph[v].sort() 
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  q = deque([v])           
  visited[v] = True
  
  while q:
    a = q.popleft()
    print(a, end=' ')
    graph[a].sort()
    
    for i in graph[a]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        
dfs(v)
print()
visited = [False] * (n+1) # 초기화
bfs(v)