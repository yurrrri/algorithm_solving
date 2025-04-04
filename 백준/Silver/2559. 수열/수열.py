import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
sliding_window = sum(arr[:k])
answer = sliding_window

for i in range(n-k):
  sliding_window -= arr[i]
  sliding_window += arr[i+k]
  answer = max(answer, sliding_window)

print(answer)