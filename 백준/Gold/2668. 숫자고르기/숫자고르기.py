import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
  global result
  
  cycle.append(node)
  visited[node] = True
  next = graph[node]

  if visited[next]:
    if next in cycle:
      result += cycle[cycle.index(next):]
      return
  else:
    dfs(next)
  
n = int(input())
graph = [0]

for a in range(1, n+1):
  b = int(input())
  graph.append(b)

visited = [False] * (n+1) # 노드 방문 여부 확인

result = [] # 결과 집합
for i in range(1, n+1):
  if not visited[i]:
    cycle = []
    dfs(i)

print(len(result))
for i in sorted(result):
  print(i)