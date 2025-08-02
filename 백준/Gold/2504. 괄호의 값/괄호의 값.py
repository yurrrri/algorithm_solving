stack = []
answer = 0
str = input()
flag = False
temp = 1

for i, w in enumerate(str):
  if w == "(":
    stack.append(w)
    temp *= 2
  elif w == "[":
    stack.append(w)
    temp *= 3
  elif w == ")":
    if not stack or stack[-1] == "[":
      flag = True
      break

    if str[i-1] == "(":
      answer += temp
    stack.pop()
    temp //= 2
  else:
    if not stack or stack[-1] == "(":
      flag = True
      break
    if str[i-1] == "[":
      answer += temp
    stack.pop()
    temp //= 3

if flag or stack:
  print(0)
else:
  print(answer)