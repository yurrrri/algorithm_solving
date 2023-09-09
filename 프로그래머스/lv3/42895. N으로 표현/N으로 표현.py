answer = 9

def solution(N, number):
    
    def dfs(count, result):
        global answer
        if count >= 9:
            return
        
        if result == number:
            answer = min(answer, count)
            return
        
        temp = 0
        for i in range(1, 10):
            temp = 10*temp + N
            dfs(count + i, result + temp)
            dfs(count + i, result - temp)
            dfs(count + i, result * temp)
            dfs(count + i, result // temp)
            
    dfs(0, 0)
    
    if answer >= 9:
        return -1
    else:
        return answer