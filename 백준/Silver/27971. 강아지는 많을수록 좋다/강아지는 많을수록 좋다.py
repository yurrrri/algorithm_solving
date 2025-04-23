from collections import deque
# n: 키우길 원하는 강아지의 수
# m: 닫힌구간의 갯수
n, m, a, b = map(int, input().split())
closed_area = []
visited = [-1] * (n+1)    # 초기에 -1을 선언함으로써 방문여부와 거리를 모두 판단할 수 있도록 함
for _ in range(m):
  l, r = map(int, input().split())
  for i in range(l, r+1):     # 닫힌 구간은 방문하지 않아야하는 곳이므로 먼저 방문처리함
    visited[i] = 0

q = deque([0])
visited[0] = 0
while q:
  dogs = q.popleft()

  for c in [a, b]:
    sum = dogs + c    # 기존에 가지고있던 강아지에 A 생성 마법 혹은 B 생성마법 수행하여 강아지 생성
    if 1 <= sum <= n and visited[sum] == -1:   # 합이 n 이내에 있으면서 방문거리를 계산한 적이 없는 경우
      q.append(sum)
      visited[sum] = visited[dogs] + 1   # 방문처리 및 행동횟수 갱신

print(visited[n] if visited[n] > 0 else -1)  # n마리의 강아지를 만들 수 없다면 -1 출력