def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(arr, airport):
        if False not in visited:
            answer.append(arr)
            return
        for i in range(len(tickets)):
            if not visited[i]:
                if tickets[i][0] == airport:
                    visited[i] = True
                    dfs(arr + [tickets[i][1]], tickets[i][1])
                    visited[i] = False
    
    dfs(["ICN"], "ICN")
    answer.sort()
    
    return answer[0]