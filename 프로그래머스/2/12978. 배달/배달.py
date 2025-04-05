import heapq

def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    q = []
    
    for a, b, c in road:
        graph[a].append((b, c))   # 양방향으로 연결
        graph[b].append((a, c))
    
    distance[1] = 0   # 1번 마을에서 시작
    heapq.heappush(q, (0, 1))    # 1번 마을이 시작점이므로, 0으로 초기화
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:   # 이미 계산한 노드라면 계산을 건너뜀
            continue
            
        for next_node, next_cost in graph[now]:       # 인접한 노드들 간의 모든 최단거리 구하기
            cost = dist + next_cost
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                
    answer = 0

    for i in distance:
        if i<=K:
            answer += 1

    return answer