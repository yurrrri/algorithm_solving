from collections import deque

def differentCount(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            
    return count

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = {}
    visited[begin] = False
    for w in words:
        visited[w] = False
    q = deque([(begin, 0)])
    while q:
        w, c = q.popleft()
        
        if w == target:
            return c
        
        for wo in words:
            if not visited[wo] and differentCount(w, wo) == 1:
                q.append((wo, c + 1))
                visited[wo] = True
    