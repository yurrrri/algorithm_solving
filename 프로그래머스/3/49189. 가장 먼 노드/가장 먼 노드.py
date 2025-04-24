from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])
    distance[1] = 1    # 방문처리
    while q:
        a = q.popleft()
        
        for node in graph[a]:
            if not distance[node]:
                distance[node] = distance[a] + 1   # 인접한 노드가 1과 연결된 간선의 갯수에 +1을 함
                q.append(node)
    
    max_vertex = max(distance)
    
    return distance.count(max_vertex)