from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
viruses = []
answer = int(1e9)

for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
    for j in range(n):
        if board[i][j] == 2:
            viruses.append((i, j))
            board[i][j] = 0   # 빈 칸으로 취급 (활성/비활성 구분은 조합으로 해결)

def bfs(virus):
    q = deque(virus)
    visited = [[False]*n for _ in range(n)]
    for x, y, _ in q:
        visited[x][y] = True

    maxvalue = 0

    while q:
        x, y, c = q.popleft()
        maxvalue = max(maxvalue, c)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # ❗ 핵심 수정: 벽(1)만 막고, 0/2는 모두 지나갈 수 있도록 함
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny, c+1))

    # 모든 '빈 칸(=0)'이 감염됐는지 체크
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and not visited[i][j]:
                return -1

    return maxvalue

for combi in combinations(viruses, m):
    virus = []
    for x, y in combi:
        virus.append((x, y, 0))
    result = bfs(virus)
    if result != -1:
        answer = min(answer, result)

print(answer if answer != int(1e9) else -1)
