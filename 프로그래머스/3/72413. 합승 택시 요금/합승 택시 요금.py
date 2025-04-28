import heapq

def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    
    for i, j, cost in fares:
        graph[i].append((j, cost))
        graph[j].append((i, cost))
    
    def dijkstra(start, end):
        distance = [INF] * (n+1)
        distance[start] = 0
        
        q = []
        heapq.heappush(q, (0, start))
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            for next_node, next_cost in graph[now]:
                cost = dist + next_cost
                
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
                    
        return distance[end]
                    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
    return answer