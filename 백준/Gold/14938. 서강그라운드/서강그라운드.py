import heapq

n, m, r = map(int, input().split())  # 지역의 갯수, 수색 범위, 길의 갯수
items = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(r):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
answer = 0

def dijkstra(start):
  distance = [INF] * (n+1)
  distance[start] = 0

  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if dist < distance[now]:
      continue

    for d, c in graph[now]:
      next_cost = c + dist
      if next_cost < distance[d]:
        distance[d] = next_cost
        heapq.heappush(q, (next_cost, d))

  return distance

for i in range(1, n+1):
  distance = dijkstra(i)
  count = 0
  for j in range(1, n+1):
    if i == j or distance[j] <= m:
        count += items[j-1]

  answer = max(count, answer)

print(answer)