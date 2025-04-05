def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        
        for i in range(n):
            if i != v and not visited[i] and computers[v][i] == 1:
                dfs(i)
        
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer