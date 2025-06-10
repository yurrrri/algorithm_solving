answer = 1e9

def solution(N, number):
    
    def dfs(count, result):
        global answer
        if count >= 9:
            return
        
        if result == number:
            answer = min(answer, count)
            return
        
        for i in range(1, 10):
            temp = int(str(N) * i)
            dfs(count + i, result + temp)
            dfs(count + i, result - temp)
            dfs(count + i, result * temp)
            dfs(count + i, result // temp)
            
    dfs(0, 0)
    
    if answer > 8:
        return -1
    else:
        return answer