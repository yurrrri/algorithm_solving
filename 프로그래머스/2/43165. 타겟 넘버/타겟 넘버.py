answer = 0

def solution(numbers, target):
    
    def dfs(depth, sum, index):     
        global answer
        
        if depth == len(numbers) and sum == target:
            answer += 1
            return
        
        if index >= len(numbers):
            return
            
        dfs(depth+1, sum + numbers[index], index+1)
        dfs(depth+1, sum - numbers[index], index+1)
        
    dfs(0, 0, 0)
    
    return answer