import sys

input = sys.stdin.readline
str = input().rstrip()
boom = list(input().rstrip())

stack = []

for i in str:   # 1_000_000보다 작거나 같음
  stack.append(i)

  while len(stack) >= len(boom) and stack[-len(boom):] == boom:
    stack[-len(boom):] = []
  
if not stack:
  print("FRULA")
else:
  print(''.join(stack))