import math

n, p = map(int, input().split())  # 방의 개수, 초기 공격력
arr = []
for _ in range(n):
  t, a, h = map(int, input().split())
  arr.append((t, a, h))
  # t가 1이면 공격력 a, 생명력 h인 몬스터
  # t가 2이면 공격력 a, 생명력 h증가 포션

def can_clear(atk, maxhp):
  current_hp = maxhp
  
  for t, a, h in arr:
    if t == 2:
      atk += a
      current_hp += h
      current_hp = min(current_hp, maxhp)   # 용사 생명력이 최대 생명력(maxhp)를 넘으면 maxhp
    else:
      current_hp -= (math.ceil(h/atk)-1) * a
  
      if current_hp <= 0:
        return False
  
  return True

start, end = 1, n*int(1e12)
answer = 0

while start <= end:
  mid = (start + end) // 2

  if can_clear(p, mid):
    answer = mid
    end = mid - 1   # 범위를 더 낮춰보기
  else:
    start = mid + 1

print(answer)