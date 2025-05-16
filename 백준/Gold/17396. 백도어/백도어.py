import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
can_go = list(map(int, input().split()))
can_go[-1] = 0    # n-1 번째 분기점은 상대의 시야게 보이게 되나, 갈 수 있는곳이므로 편의상 도착지점을 0으로 지정한다.
graph = [[] for _ in range(n)]
distance = [INF] * n
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

q = []
start = 0
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
  cost, node = heapq.heappop(q)

  if distance[node] < cost:
    continue

  for nb_n, nb_c in graph[node]:
    next_cost = nb_c + cost
    if distance[nb_n] > next_cost and can_go[nb_n] == 0:
      distance[nb_n] = next_cost
      heapq.heappush(q, (next_cost, nb_n))

print(distance[-1] if distance[-1] != INF else -1)