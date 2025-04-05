from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(v):
        q = deque([v])
        visited[v] = True
        
        while q:
            node = q.popleft()
        
            for i in range(n):
                if i != node and not visited[i] and computers[node][i] == 1:
                    q.append(i)
                    visited[i] = True
        
        
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
    return answer