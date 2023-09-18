import sys, heapq

n,m,k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c)) # 양방향 도로
    graph[b].append((a,c))
    
INF = 9888888777777666

# d : 2차원 다익스트라 배열. 현재 정점 i에서 포장을 j개 했을 때 드는 최소거리
distance = [[INF] * (k + 1) for _ in range(n + 1)]
q = []
for i in range(k + 1):
    distance[1][i] = 0
heapq.heappush(q, (0,1,0))

while q:
    dist, now, p = heapq.heappop(q)
  
    if distance[now][p] < dist:
        continue

    # 포장을 하는 경우
    if p + 1 <= k:
        for (next, next_dist) in graph[now]:
            if distance[next][p + 1] > dist:
                distance[next][p + 1] = dist
                heapq.heappush(q, (dist, next, p + 1))
                
    # 기본적으로 포장을 하지 않는 경우
    for (next, next_dist) in graph[now]:
        if distance[next][p] > dist + next_dist:
            distance[next][p] = dist + next_dist
            heapq.heappush(q, (dist + next_dist, next, p))

ans = INF
for i in range(k + 1):
    ans = min(ans, distance[n][i])
print(ans)