import heapq
import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
  input = int(sys.stdin.readline().rstrip())
  if input == 0:
    if len(arr) == 0:
      print(0)
    else:
      print(-(heapq.heappop(arr)))
  else:
    heapq.heappush(arr, -input)