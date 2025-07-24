n, k = map(int, input().split())
# 내구도가 0인 칸의 갯수가 k개 이상이라면 멈춤
conveyor = list(map(int, input().split()))
robots = [0] * 2*n
step = 1

while True:
  # 한칸 회전한다.
  conveyor.insert(0, conveyor.pop())
  robots.insert(0, robots.pop())

  # 언제든지 로봇이 내리는 위치에 도달하면 내린다.
  robots[n-1] = 0

  # 가장 먼저 벨트에 올라가있는 로봇 -> 역순 탐색
  for i in range(2*n-1, -1, -1):
    if robots[i] == 1:
      if i == 2*n-1:
        ni = 0
      else:
        ni = i + 1
      if robots[ni] == 0 and conveyor[ni] >= 1:   # 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상
        robots[i] = 0   # 로봇 이동
        robots[ni] = 1
        conveyor[ni] -= 1

  # 언제든지 로봇이 내리는 위치에 도달하면 내린다.
  robots[n-1] = 0

  if conveyor[0] > 0:  # 올리는 위치의 내구도가 0이 아니면 로봇 올리기
    conveyor[0] -= 1
    robots[0] = 1

  count = 0
  for c in conveyor:
    if c == 0:
      count += 1

  if count >= k:
    break

  step += 1

print(step)