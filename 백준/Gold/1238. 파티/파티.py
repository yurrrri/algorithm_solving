import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  graph[a].append((b,c))

def dijkstra(start, end):
  global n
  
  q = []
  distance = [INF] * (n+1) # start에서 인덱스 1~n까지 가기까지의 최단거리를 저장할 배열 --> 처음에는 Inf로 초기화
  distance[start] = 0
  heapq.heappush(q, (0, start))  # 처음에는 힙에 시작점, 0 넣기
  _max = 0

  while q:
    dist, now = heapq.heappop(q)  # 현재의 거리와 노드

    if distance[now] < dist: # 현재의 거리가 꺼낸 거리보다 작다면, 넘어감
      continue

    for node, c in graph[now]:  # now 노드에 연결된 그래프 중에서 최단거리를 가지는 노드가 있는지 확인
      cost = dist + c
      if cost < distance[node]:
        distance[node] = cost
        heapq.heappush(q, (cost, node))

  return distance[end]

for i in range(1, n+1):
  go = dijkstra(i, x)
  back = dijkstra(x, i)
  answer = max(answer, go + back)
print(answer)