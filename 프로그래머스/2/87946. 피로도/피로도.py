answer = -1

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def backtrakcing(k, count):
        
        global answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                backtrakcing(k - dungeons[i][1], count+1)
                visited[i] = False
                
    backtrakcing(k, 0)
                
    return answer