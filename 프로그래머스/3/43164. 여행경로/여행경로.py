def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(v, arr):
        if len(arr) == len(tickets) + 1:
            answer.append(arr)
            return
        
        for i, [start, end] in enumerate(tickets):
            if start == v and not visited[i]:
                visited[i] = True
                dfs(end, arr + [end])
                visited[i] = False
                
    dfs("ICN", ["ICN"])
    answer.sort()
                
    return answer[0]