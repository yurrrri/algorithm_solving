n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0  # 지금까지 측정 가능한 최대 무게 (초기: 0)

for w in arr:
    if w > answer + 1:
      break
    answer += w  # 기존 구간 확장

print(answer + 1)  # 끝까지 연결되었으면 다음 숫자부터 측정 불가