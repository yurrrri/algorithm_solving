from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 0, 1, 0]   # 상-좌-하-우 offset
    dy = [0, -1, 0, 1]
    INF = int(1e9)
    visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    q = deque()
    for i in range(4):         # 처음의 모든 방향을 0으로 초기화
        q.append((0, 0, i, 0))
        visited[0][0][i] = 0
    
    def is_valid(x, y):     # 도로를 설치할 수 있는지 판단해주는 함수
        if 0<=x<n and 0<=y<n and board[x][y] == 0:
            return True
        return False
    
    def calculate_cost(prev, current):
        if abs(prev-current) % 2 == 0:   # 상-하, 좌-우 등 같은 방향일 경우의 직선 도로 비용
            return 100
        else:    # 다를 경우 코너로 꺾어야하므로 코너 비용 100 + 500
            return 600
        
    # BFS 실행시, 최소 비용을 계산할때 방문시마다 어떤 정보가 필요한지를 판단하고 큐와 visited 배열을 설계해야한다.
    while q:
        x, y, prev_dir, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            new_cost = cost + calculate_cost(prev_dir, i)
            
            if is_valid(nx, ny) and visited[nx][ny][i] > new_cost:    # 방문한 적이 없거나(INF), new_cost가 기존 비용보다 더 작으면 이걸로 갱신
                # 기존 비용(visited[nx][ny][i])과 비교하는 이유는 방향에 따라 비용이 달라지기 때문
                visited[nx][ny][i] = new_cost
                q.append((nx, ny, i, new_cost))
    
    return min(visited[n-1][n-1])