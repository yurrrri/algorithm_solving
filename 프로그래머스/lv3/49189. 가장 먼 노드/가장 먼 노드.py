from collections import deque

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    q = deque()
    q.append(1)
    distance[1] = 0
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if distance[i] > distance[now] + 1:
                distance[i] = distance[now] + 1
                q.append(i)
                
    distance = list(filter(lambda x:x != INF, distance))
    mx = max(distance)
    
    for i in distance:
        if i == mx:
            answer +=1
    
    return answer