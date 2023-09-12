from collections import deque

def solution(board):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    
    def bfs(i, j, c, path):
        visited = [[0] * n for _ in range(n)]  # 방문 여부와 기존의 최소값을 저장할 배열
        q = deque([(i, j, c, path)])  # path: 위치 정보를 알고있어야 코너 / 직선도로 중 선택해서 세울 수 있음
        
        while q:
            x, y, c, path = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    if path == i:  # 직선
                        newcost = c + 100
                    else: # 꺽임 --> 600 추가
                        newcost = c + 600
                        
                    if not visited[nx][ny] or (visited[nx][ny] > newcost):
                        # 방문한 적이 없거나, newcost가 기존의 값보다 더 쌀 때 (경주로를 건설하는 데 최소 비용을 구하는 문제이므로, 더 싸게 건설할 수 있는 비용이 있다면 갱신해주어야함)
                        q.append((nx, ny, newcost, i)) # 탐색범위에 추가
                        visited[nx][ny] = newcost # 더 싼 값으로 갱신하고
                        
        return visited[n-1][n-1]
    
    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 3))  
# 시작점에서 가로로 출발할때와 세로로 출발할때를 비교하여 최소값 반환