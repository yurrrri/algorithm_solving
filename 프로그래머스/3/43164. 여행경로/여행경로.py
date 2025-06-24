def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(v, arr):
        if len(arr) == len(tickets) + 1:   # 주어진 항공권은 모두 사용해야한다
            answer.append(arr)
            return
        
        for i, [start, end] in enumerate(tickets):
            if start == v and not visited[i]:
                visited[i] = True     # 해당 티켓을 사용했다가
                dfs(end, arr + [end])
                visited[i] = False    # 복원
                
    dfs("ICN", ["ICN"])
    answer.sort()
                
    return answer[0]