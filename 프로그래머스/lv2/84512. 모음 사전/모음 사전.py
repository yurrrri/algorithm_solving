def solution(word):
    answer = []
    
    def dfs(w, length):
        if length > 5:
            return
        answer.append(w)
        
        for i in ["A", "E", "I", "O", "U"]:
            dfs(w + i, length+1)
            
    dfs("", 0)        
        
    return answer.index(word)