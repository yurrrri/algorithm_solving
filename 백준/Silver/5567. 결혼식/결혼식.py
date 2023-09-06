from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  visited[v] = 1
  q = deque([v])

  while q:
    x = q.popleft()

    if x != 1 and visited[x] < 4:
      answer.append(x)

    for i in graph[x]:
      if not visited[i]:
        visited[i] = visited[x] + 1
        q.append(i)

bfs(1)
print(len(answer))