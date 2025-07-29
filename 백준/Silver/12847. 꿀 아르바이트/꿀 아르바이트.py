n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
_sum = sum(arr[:m])
answer = max(answer, _sum)

for i in range(n-m):
  _sum -= arr[i]
  _sum += arr[i+m]
  answer = max(_sum, answer)

print(answer)