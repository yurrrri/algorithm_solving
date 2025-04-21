# 다익스트라
# import heapq

# def solution(board):
#     n = len(board)
#     INF = int(1e9)
#     # 방향: 차례대로 상 좌 하 우
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
    
#     # 3차원 거리 배열: [x][y][dir]
#     distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
#     # 초기 위치 (0, 0) 에 대해 모든 방향 비용 0으로 초기화
#     for i in range(4):
#         distance[0][0][i] = 0
    
#     heap = []
#     heapq.heappush(heap, (0, -1, 0, 0))  # 비용, 이전방향, x, y

#     def calculate_cost(direction, prev_direction, cost):
#         if prev_direction == -1 or (prev_direction - direction) %2 == 0:
#             return cost + 100
#         else:
#             return cost + 600

#     while heap:
#         cost, direction, x, y = heapq.heappop(heap)

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
#                 next_cost = calculate_cost(i, direction, cost)
#                 if distance[nx][ny][i] > next_cost:
#                     distance[nx][ny][i] = next_cost
#                     heapq.heappush(heap, (next_cost, i, nx, ny))

#     return min(distance[n - 1][n - 1])  # 도착점까지의 최소 비용

# BFS
from collections import deque

def solution(board):
    n = len(board)
    INF = 1e9
    
    # 방향: 상(0), 좌(1), 하(2), 우(3)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 3차원 거리 배열: [x][y][dir]
    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    # 초기 위치에서 네 방향 모두 시작 가능
    q = deque([])
    for i in range(4):
        distance[0][0][i] = 0
        q.append((0, 0, i, 0))  # x, y, 방향, 비용

    def calculate_cost(direction, prev_direction, cost):
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        else:
            return cost + 600

    while q:
        x, y, direction, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                next_cost = calculate_cost(i, direction, cost)
                if distance[nx][ny][i] > next_cost:
                    distance[nx][ny][i] = next_cost
                    q.append((nx, ny, i, next_cost))

    return min(distance[n - 1][n - 1])
