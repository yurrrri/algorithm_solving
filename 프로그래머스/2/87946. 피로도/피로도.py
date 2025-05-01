answer = -1

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(power, num):
        global answer
        
        answer = max(answer, num)
        
        for i in range(len(dungeons)):
            if not visited[i] and power >= dungeons[i][0]:
                visited[i] = True
                dfs(power - dungeons[i][1], num+1)
                visited[i] = False
                
    dfs(k, 0)
        
    return answer