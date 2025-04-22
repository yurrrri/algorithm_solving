from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)  # 거리 기록용 (-1은 방문 안함 의미)
    distance[1] = 0  # 1번 노드는 거리 0으로 시작

    queue = deque([1])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    max_dist = max(distance)
    return distance.count(max_dist)