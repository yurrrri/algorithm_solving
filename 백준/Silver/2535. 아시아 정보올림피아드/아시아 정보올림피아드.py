n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[2], reverse=True)

print(arr[0][0], arr[0][1])
print(arr[1][0], arr[1][1])

for nation, number, score in arr[2:]:
  if nation == arr[0][0] == arr[1][0]:
    continue

  print(nation, number)
  break