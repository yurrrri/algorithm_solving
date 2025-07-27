import sys
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    answer = ""
    dic = {"l": (0, -1), "r": (0, 1), "u": (-1, 0), "d": (1, 0)}
    
    def dfs(pos_x, pos_y, route):
        nonlocal answer
        
        if len(route) == k and pos_x == r and pos_y == c:
            answer = route
            return
        
        if answer:
            return

        remain = k - len(route)    # 남은 이동횟수
        d = abs(pos_x - r) + abs(pos_y - c)   # 현재 위치에서 목표 지점까지의 거리
        if d > remain or (remain - d) % 2 != 0:
            return
        
        for i in ["d", "l", "r", "u"]:   # 사전 순으로 빠른 경로를 만들기 위해 d, l, r, u 순서대로 만듦
            nx = pos_x + dic[i][0]
            ny = pos_y + dic[i][1]
            
            if 1<=nx<=n and 1<=ny<=m:
                dfs(nx, ny, route + i)
                
    dfs(x, y, "")
    
    if not answer:
        return "impossible"
    else:
        return answer