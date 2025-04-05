import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())  # 정점의 갯수 v, 간선의 갯수 e
start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)   # 시작노드부터 특정 노드까지의 최소비용 저장 테이블 --> 초기에는 모두 INF로 초기화함

for _ in range(e):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))   #u에서 v로 가는 가중치 w인 간선

def dijkstra(start):
  q = []
  distance[start] =  0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
          distance[i[0]] = cost
          heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, len(distance)):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])