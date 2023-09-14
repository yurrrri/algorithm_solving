import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

dic = defaultdict(int)

start = 0
end = 0

dic[arr[start]] = 1
answer = int(1e9)

while end < n:
  if dic[1] < k:
    end += 1
    if end >= n:
      break
    dic[arr[end]] += 1
  else:
    answer = min(answer, end - start + 1)
    dic[arr[start]] -= 1
    start += 1

if answer == int(1e9):
  print(-1)
else:
  print(answer)