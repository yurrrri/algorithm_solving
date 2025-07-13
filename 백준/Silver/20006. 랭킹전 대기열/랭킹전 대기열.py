rooms = []
p, m = map(int, input().split())  # 플레이어의 수, 방의 정원
room = []

for i in range(p):
  l, n = input().split()   # 플레이어의 레벨 l, 닉네임 n
  l = int(l)
  flag = False
  for room in rooms:
    for _, _, standard in room:
      if standard-10 <= l <=standard+10 and len(room) < m:
        room.append((l, n, standard))
        flag = True
        break
    if flag:
      break

  if not flag:
    room = []
    room.append((l, n, l))
    rooms.append(room)

for room in rooms:
  room.sort(key=lambda x:x[1])

for room in rooms:
  if len(room) == m:
    print("Started!")
  else:
    print("Waiting!")
  for level, nickname, _ in room:
    print(f"{level} {nickname}")