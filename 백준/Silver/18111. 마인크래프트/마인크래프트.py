import sys
input = sys.stdin.readline

n, m, b = map(int, input().rstrip().split())   # b: 초기 블럭의 개수
board = []

for _ in range(n):
  board.append(list(map(int, input().split())))

mintime = 500*500*257*2  # 땅을 고르게 하는 데 드는 최대의 시간
answerHeight = 0   # 땅이 모두 고르게 될 때의 최소 높이

for height in range(257): # 땅의 높이는 0~256 사이
    use_block = 0  #떼가는 블럭의 수
    take_block = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] >= height: # 블럭을 떼가야함
              # 오답노트 1. board[x][y] - height인 이유?
              # 블럭은 1x1x1 크기의 네모이기 때문에, board[x][y] - height값이 곧 빼내야할 블럭의 개수라고 볼 수 있음 -> 인벤토리에 포함되는 블럭의 개수
                take_block += board[x][y] - height
            else:
              # 올려야 하는 블럭의 개수 -> 인벤토리에 빠져나가는 블럭의 개수
                use_block += height - board[x][y]

  # 오답노트 2. if use_block <= take_block + b
  # 인벤토리에 있는 블럭을 사용해서 높이가 모자란 블럭에 쌓을 수 있어야하므로 해당 조건문을 써야함
  
    if use_block <= take_block + b:
      time = take_block * 2 + use_block #시간 계산
      if time <= mintime:  # 만약 시간이 기존의 최소시간보다 작다면? 시간과 높이 저장
        mintime = time
        answerHeight = height


print(mintime, answerHeight)