from collections import deque

n, m, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
INF = int(1e9)

for _ in range(n):
    board.append(list(map(int, list(input()))))

# Initialize visited array correctly
visited = [[[INF for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

q = deque([(0, 0, 0)])  # (x, y, wall_breaks_used)
visited[0][0][0] = 1    # Start with 0 walls broken

while q:
    x, y, wall = q.popleft()
    
    # If we've reached the destination, no need to explore further
    if x == n-1 and y == m-1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # Check bounds
        if not (0 <= nx < n and 0 <= ny < m):
            continue
            
        # Empty cell case
        if board[nx][ny] == 0 and visited[nx][ny][wall] == INF:
            visited[nx][ny][wall] = visited[x][y][wall] + 1
            q.append((nx, ny, wall))
            
        # Wall case - can we break it?
        elif board[nx][ny] == 1 and wall < k and visited[nx][ny][wall+1] == INF:
            visited[nx][ny][wall+1] = visited[x][y][wall] + 1
            q.append((nx, ny, wall+1))

# Find the minimum path length at the destination
result = min(visited[n-1][m-1])
print(result if result != INF else -1)