import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
levels = []

for _ in range(n):   # 10^5
  name, limit = input().rstrip().split()
  levels.append((name, int(limit)))

for _ in range(m):
  level = int(input())
  left = 0
  right = n-1
  answer = 0

  while left <= right:
    mid = (left + right) // 2

    if level > levels[mid][1]:
      left = mid + 1
    else:
      right = mid - 1
      answer = mid

  print(levels[answer][0])