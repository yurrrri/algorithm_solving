answer = 0

def solution(numbers, target):
    
    def dfs(depth, count, index):     
        global answer
        
        if depth == len(numbers) and count == target:
            answer += 1
            return
        
        if index >= len(numbers):
            return
            
        dfs(depth+1, count + numbers[index], index+1)
        dfs(depth+1, count - numbers[index], index+1)
        
    dfs(0, 0, 0)
    
    return answer