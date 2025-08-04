n = int(input())
arr = []
answer = 0
for _ in range(n):
  arr.append(int(input()))
arr.sort(reverse=True)

for i in range(0, n, 3):
  temp = arr[i:i+3]
  if len(temp) == 3:
    answer += sum(temp) - temp[2]
  else:
    answer += sum(temp)

print(answer)