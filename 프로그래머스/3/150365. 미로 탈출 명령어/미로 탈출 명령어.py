import sys
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    answer = ""
    dic = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}
    
    def dfs(pos_x, pos_y, route):
        nonlocal answer
        
        if len(route) == k and pos_x == r-1 and pos_y == c-1:
            answer = route
            return
        
        if answer:
            return

        remain = k - len(route)
        d = abs(pos_x - (r-1)) + abs(pos_y - (c-1))
        if d > remain or (remain - d) % 2 != 0:
            return
        
        for i in ["d", "l", "r", "u"]:
            nx = pos_x + dic[i][0]
            ny = pos_y + dic[i][1]
            
            if 0<=nx<n and 0<=ny<m:
                dfs(nx, ny, route + i)
                
    dfs(x-1, y-1, "")
    
    if not answer:
        return "impossible"
    else:
        return answer