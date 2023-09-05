import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(node):
  global count
  
  cycle.append(node)
  visited[node] = True
  pair = graph[node]
  
  if visited[pair]: #방문가능한 곳이 끝났는지
      if pair in cycle: #사이클 가능 여부
          count += len(cycle[cycle.index(pair):]) #사이클 되는 구간 부터만 팀을 이룸
      return
  else:
      dfs(pair)
  
for _ in range(t):
  n = int(input()) # 학생의 수
  graph = [0] * (n+1)
  arr = list(map(int, input().rstrip().split()))
  for i in range(1, n+1):
    graph[i] = arr[i-1]
  count = 0
  visited = [False] * (n+1)
  for i in range(1, n+1):
    if not visited[i]:
      cycle = []
      dfs(i)

  print(n - count)