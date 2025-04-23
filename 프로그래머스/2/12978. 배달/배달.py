import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    answer = 0
    INF = 1e9
    distance = [INF] * (N+1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))   # 비용이 앞에 오도록 !
    
    while q:
        cost, node = heapq.heappop(q)
        
        if distance[node] < cost:
            continue
            
        for next_node, next_cost in graph[node]:
            total = cost + next_cost
            if total < distance[next_node]:
                distance[next_node] = total
                heapq.heappush(q, (total, next_node))

    for c in distance:
        if c <= K:
            answer += 1
            
    return answer