def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(v):
        visited[v] = True
        cnt = 1
        
        for node in graph[v]:
            if not visited[node]:
                cnt += dfs(node)
                
        return cnt
                
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        cnt_a = 0
        visited = [False] * (n+1)
        
        for i in range(1, n+1):
            if graph[i] and not visited[i]:
                cnt_a = dfs(i)
                
        cnt_b = n - cnt_a
        answer = min(answer, abs(cnt_b - cnt_a))
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer