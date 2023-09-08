def solution(n, computers):
    answer = 0
    visited = [0] * len(computers)
    
    def dfs(v):
        visited[v] = True
        
        for i in range(n):
            if computers[v][i] == 1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer