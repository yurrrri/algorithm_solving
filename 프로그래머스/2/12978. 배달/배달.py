import heapq
import sys

def solution(N, road, K):
    answer = 0
    INF = sys.maxsize
    
    distance = [INF] * (N+1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    graph = [[] * (N+1) for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    while q:
        cost, node = heapq.heappop(q)
        
        if distance[node] < cost:
            continue
            
        for v, c in graph[node]:
            if cost + c < distance[v]:
                distance[v] = cost + c
                heapq.heappush(q, (cost+c, v))
    
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer