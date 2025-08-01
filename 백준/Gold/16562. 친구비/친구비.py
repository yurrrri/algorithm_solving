import sys
sys.setrecursionlimit(10**8)

n, m, k = map(int, input().split())
money = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
  v, w = map(int, input().split())
  graph[v].append(w)
  graph[w].append(v)

def dfs(node):
  global temp
  
  visited[node] = True
  temp = min(temp, money[node])

  for i in graph[node]:
    if not visited[i]:
      dfs(i)

answer = 0

visited = [False] * (n+1)
for i in range(1, n+1):
  if not visited[i]:
    temp = 1e9
    dfs(i)
    answer += temp

if answer <= k:
  print(answer)
else:
  print("Oh no")