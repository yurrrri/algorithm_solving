import heapq

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start, end):
  global n
  
  q = []
  distance = [INF] * (n+1)
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    current_cost, current_node = heapq.heappop(q)
  
    if distance[current_node] < current_cost:
      continue
  
    for next_node, next_cost in graph[current_node]:
      new_cost = next_cost + current_cost
      if new_cost < distance[next_node]:
        distance[next_node] = new_cost
        heapq.heappush(q, (new_cost, next_node))

  return distance[end]

res1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
res2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if res1 >= INF and res2 >= INF:
  print(-1)
else:
  print(min(res1, res2))