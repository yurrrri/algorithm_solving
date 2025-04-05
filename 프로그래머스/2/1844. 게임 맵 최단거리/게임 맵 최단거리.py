from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    distance = [[-1] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque([(x, y)])
        distance[x][y] = 1

        while q:
            now_x, now_y = q.popleft()

            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]

                if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 0 and distance[nx][ny] == -1:
                    q.append((nx, ny))
                    distance[nx][ny] = distance[now_x][now_y] + 1
                    
        return distance
    
    bfs(0, 0)
        
    return distance[n-1][m-1]