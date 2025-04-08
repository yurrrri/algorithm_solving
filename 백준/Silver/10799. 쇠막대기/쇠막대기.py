pipelines = input()
stack = []
answer = 0

for idx, p in enumerate(pipelines):
  if p == "(":
    stack.append("(")
  else:
    if pipelines[idx-1] == "(":   # 레이저인 경우
      stack.pop()          # 레이저 쌍이므로 pop
      answer += len(stack)   # 쇠막대의 갯수만큼 더함
    else:
      stack.pop()
      answer += 1   # 쇠막대의 끝을 더함

print(answer)