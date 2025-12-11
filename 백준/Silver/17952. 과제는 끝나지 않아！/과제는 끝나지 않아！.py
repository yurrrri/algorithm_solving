n = int(input())   # 이번학기가 몇분인지
stack = []
answer = 0

for i in range(n):
  prompt = list(map(int, input().split()))
  if prompt[0] == 1:
    stack.append((prompt[2], prompt[1]))

  if stack:
    time, score = stack.pop()
    if time-1 == 0:
      answer += score
    else:
      stack.append((time-1, score))

print(answer)