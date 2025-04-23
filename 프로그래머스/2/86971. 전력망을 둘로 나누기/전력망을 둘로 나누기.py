def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = 1e9
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)   # 양방향 그래프
        
    def dfs(v):
        visited[v] = True
        count = 1
        
        for node in graph[v]:
            if not visited[node]:
                count += dfs(node)
                
        return count
                
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        visited = [False] * (n+1)
        cnt_a = dfs(a)
        cnt_b = n - cnt_a
        
        answer = min(answer, abs(cnt_b - cnt_a))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer