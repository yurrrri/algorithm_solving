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
                # 복원하는 이유: 한 도시마다 갈 수 있는 경로가 여러가지일 경우, 가지 치기를 통해 판단해야하므로 일단 먼저 방문한 다음에 다시 원상복구해서 다른 루트를 찾을 수 있어야함
                
    dfs("ICN", ["ICN"])
    answer.sort()
                
    return answer[0]