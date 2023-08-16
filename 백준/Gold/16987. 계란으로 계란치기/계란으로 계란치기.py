import sys

input = sys.stdin.readline
n = int(input().rstrip())
eggs = []
for _ in range(n):
  naegudo, weight = map(int, input().rstrip().split())
  eggs.append([naegudo, weight]) # 내구도, 무게
answer = 0
egg = eggs[0] # 드는 계란
#1) 가장 왼쪽의 계란을 든다

def countCrahsedEgg():
  count = 0
  for i in range(n):
    if eggs[i][0] <= 0:
      count += 1
  return count

def simul(idx):
  global answer
  # print(eggs)
  crashed = countCrahsedEgg()
  answer = max(crashed, answer)
  
  if idx == n: # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란이면 종료
    return

  if eggs[idx][0] <= 0:  #손에 들고 있는 계란이 깨졌으면 오른쪽 계란으로 이동
    simul(idx+1)
    
  for i in range(n): # 손에 들고있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
    if eggs[i][0] > 0 and i != idx and eggs[idx][0] > 0:
      eggs[idx][0] -= eggs[i][1]  #서로 내구도에서 무게 감소
      eggs[i][0] -= eggs[idx][1]
      simul(idx+1) # 오른쪽 계란을 들고 2번 진행
      eggs[idx][0] += eggs[i][1]  #서로 내구도에서 무게 감소
      eggs[i][0] += eggs[idx][1]

simul(0) # 가장 왼쪽의 계란을 든다.
print(answer)