import heapq

def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    q = []
    
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    answer = 0

    for i in distance:
        if i<=K:
            answer += 1

    return answer