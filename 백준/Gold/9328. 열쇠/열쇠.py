import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 해당 열쇠로 열 수 있는 문 표시
def init_doors():
    for key in keys:
        if key == '0':
            break
        doors[ord(key) - ord('a')] = True
        
# 열 수 있는 문을 빈 공간으로 변경
def init_building():
    for i in range(1, h+1):
        for j in range(1, w+1):
            if building[i][j].isupper() and doors[ord(building[i][j].lower())-ord('a')]:
                building[i][j] = '.'
                
def bfs():
    res = 0
    visited = [[False] * w for _ in range(h)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '*' and not visited[nx][ny]:
                # 다음 포지션이 빈 공간이면 히스토리 추가 및 큐에 삽입
                if building[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    # 다음 포지션에 문서가 있으면 res 증가
                    if building[nx][ny] == '$':
                        res += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        building[nx][ny] = '.'  # 문서를 가져갔으므로 빈공간 표시
                    else:
                        # 다음 포지션에 문이 있으면 열 수 있으면 빈 공간으로 만들고 큐에 삽입
                        if building[nx][ny].isupper():
                            if doors[ord(building[nx][ny].lower())-ord('a')]:
                                building[nx][ny] = '.'
                                visited[nx][ny] = True
                                q.append((nx, ny))
                        # 다음 포지션에 열쇠가 있으면 히스토리 초기화
                        elif building[nx][ny].islower():
                            doors[ord(building[nx][ny].lower())-ord('a')] = True
                            building[nx][ny] = '.'
                            visited = [[False] * w for _ in range(h)]
                            q = deque()
                            q.append((nx, ny))
    return res

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    building = []
    # 외곽에 빈 공간 추가 --> 아무 빈 공간을 찾아서 들어갈 수 있기 위해서, 외곽을 추가해서 거기서 들어갈 수 있도록 하는것임
    building.append(['.'] * (w + 2))
    for _ in range(h):
        building.append(['.'] + list(input().rstrip()) + ['.'])
    building.append(['.'] * (w + 2))
    
    keys = list(input().rstrip())
    doors = [False] * 26
    init_doors()   # 열쇠로 열 수 있는 문을 배열 형태로 가지고 있다가 그 문들을 빈 공간으로 표시 후에 탐색 시작함
    init_building()
    
    h, w = h+2, w+2  # 외곽 추가때문에 양옆에 1씩 추가되었으므로 탐색 범위가 h+2, w+2로 변경됨
                         
    print(bfs())