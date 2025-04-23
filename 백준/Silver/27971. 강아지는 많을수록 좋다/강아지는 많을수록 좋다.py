from collections import deque
# n: 키우길 원하는 강아지의 수
# m: 닫힌구간의 갯수
n, m, a, b = map(int, input().split())
closed_area = []
visited = [0] * (n+1)
for _ in range(m):
  l, r = map(int, input().split())
  for i in range(l, r+1):
    visited[i] = 1

q = deque([0])
visited[0] = 0
while q:
  dogs = q.popleft()

  for c in [a, b]:
    sum = dogs + c
    if 1 <= sum <= n and not visited[sum]:
      q.append(sum)
      visited[sum] = visited[dogs] + 1

print(visited[n] if visited[n] else -1)  