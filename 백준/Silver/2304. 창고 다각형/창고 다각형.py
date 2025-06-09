n = int(input())
max_height = 0
left = []
right = []
arr = []

for _ in range(n):
  l, h = map(int, input().split())
  max_height = max(max_height, h)
  arr.append((l, h))

arr = sorted(arr, key=lambda x:x[0])

max_height_duo = (0, 0)
for l, h in arr:
  if h == max_height:
    max_height_duo = (l, h)

for l, h in arr:
  if l < max_height_duo[0]:
    left.append((l, h))
  else:
    right.append((l+1, h))

left.append(max_height_duo)
right.insert(0, max_height_duo)

curr = 0
answer = 0
for i in range(1, len(left)):
  curr = max(curr, left[i-1][1])
  answer += (left[i][0] - left[i-1][0]) * curr

curr = 0
for i in range(len(right)-1, 0, -1):
  curr = max(curr, right[i][1])
  answer += (right[i][0] - right[i-1][0]) * curr

print(answer)