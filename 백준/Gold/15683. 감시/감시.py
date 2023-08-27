import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#6은 벽, 0은 빈칸, 1-5는 CCTV의 번호
answer = int(1e9) # 사각 지대의 최소 크기
cctv = []
mode = [
    [],  # cctv가 회전할 때마다 가능한 방향을 0을 동쪽으로 정의 후에 리스트로 저장
    [[0], [1], [2], [3]], #1번 cctv
    [[0, 2], [1, 3]], #2번 cctv
    [[0, 1], [1, 2], [2, 3], [0, 3]], #3번 cctv
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], #4번 cctv
    [[0, 1, 2, 3]], #5번 cctv
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
  for j in range(m):
    if 1 <= board[i][j] <= 5:
      cctv.append((board[i][j], i, j))

def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not 0 <= nx < n or not 0 <= ny < m: # 범위를 벗어나면 break
                break
            if board[nx][ny] == 6: # 벽을 마주치면 멈춤
                break
            elif board[nx][ny] == 0: #빈공간이면 7을 할당하여 감시 가능한 영역으로 마킹
                board[nx][ny] = 7

def dfs(depth, arr):
    global answer

    if depth == len(cctv) :
        count = 0
        for i in range(n) :
            count += arr[i].count(0)
        answer = min(answer, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


dfs(0, board)
print(answer)