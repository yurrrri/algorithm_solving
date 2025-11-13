import heapq

def solution(N, road, K):

    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    distance[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))     # 1. 시작점의 최소 이동거리는 0
    
    while heap:
        now_cost, now_node = heapq.heappop(heap)
        
        if distance[now_node] < now_cost:   # 2. 힙에서 꺼낸 비용이 기존 distance의 거리 비용보다 크다면, 계산할 필요가 없으므로 무시한다.
            continue
            
        for node, cost in graph[now_node]:   # 3. 현재 노드에 연결된 노드의 비용과 현재 비용을 더해(new_cost) 이를 기존 distance 배열에 저장한 최소 비용과 비교한다.
            new_cost = now_cost + cost
            if now_cost + cost < distance[node]:   # 이 값이 기존의 distance 배열에 저장한 최소 비용보다 낮다면 갱신하고
                distance[node] = new_cost
                heapq.heappush(heap, (new_cost, node))   # 힙에 새로운 비용과 노드를 저장한다.
                
    return sum(1 for dist in distance if dist <= K)