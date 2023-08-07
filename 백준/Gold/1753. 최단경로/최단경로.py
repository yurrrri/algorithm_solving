import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().rstrip().split())
start = int(input().rstrip())

graph = [[] for _ in range(v+1)]  # []의 개수가 v+1개
distance = [INF] * (v+1)  # 원소의 개수가 v+1개

#1. 간선 정보 입력받기
for _ in range(e):
	u, v, w = map(int, input().rstrip().split())
	graph[u].append((v, w)) # u에서 v로 가는 비용이 w

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start)) # 시작점은 비용 0으로 해서 큐에 삽입
	distance[start] = 0
	
	while q:
		dist, now = heapq.heappop(q) # 차례대로 거리, 정점

		if distance[now] < dist:
			continue

		for i in graph[now]:  # 정점, 거리
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