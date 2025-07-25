import sys
sys.setrecursionlimit(10**8)

def solution(land):
    answer = 0
    n = len(land)   # n: 세로길이 - x
    m = len(land[0])  # m: 가로길이 - y
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num = 0   # 덩어리를 구분짓기 위한 숫자
    land_num = [[0] * m for _ in range(n)]
    arr = []
    
    def dfs(x, y):
        visited[x][y] = True
        temp.append((x, y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and land[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)
                
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                num += 1
                temp = []
                dfs(i, j)
                size = len(temp)
                arr.append([num, size, temp])
                
    for num, size, poses in arr:
        for x, y in poses:
            land[x][y] = size
            land_num[x][y] = num
                                        
    for i in range(m):
        oil_set = set()
        for j in range(n):
            if land[j][i] != 0:
                oil_set.add((land_num[j][i], land[j][i]))
        # print(oil_set)
                
        _sum = 0
        for num, amount in oil_set:
            _sum += amount
                
        answer = max(answer, _sum)
    
    return answer