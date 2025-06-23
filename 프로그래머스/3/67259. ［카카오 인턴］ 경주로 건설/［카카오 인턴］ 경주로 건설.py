from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 0, 1, 0]   # 상-좌-하-우 offset
    dy = [0, -1, 0, 1]
    visited = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
    q = deque([])
    for i in range(4):
        q.append((0, 0, i, 0))
        visited[0][0][i] = 0
    
    def is_valid(x, y):
        if 0<=x<n and 0<=y<n and board[x][y] == 0:
            return True
        else:
            return False
    
    def calculate_cost(prev, current):
        if prev == -1 or abs(prev-current) % 2 == 0:
            return 100
        else:
            return 600
        
    while q:
        x, y, prev_dir, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            new_cost = cost + calculate_cost(prev_dir, i)
            
            if is_valid(nx, ny) and (visited[nx][ny][i] == -1 or visited[nx][ny][i] > new_cost):
                visited[nx][ny][i] = new_cost
                q.append((nx, ny, i, new_cost))
    
    return min([c for c in visited[n-1][n-1] if c != -1])