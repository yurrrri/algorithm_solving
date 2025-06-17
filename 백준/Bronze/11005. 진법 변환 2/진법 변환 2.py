n, b = map(int, input().split())
stack = []

while n > 0:
  remain = n%b
  if remain >= 10:
    remain = chr(remain - 10 + ord('A'))
  stack.append(str(remain))
  n //= b

print("".join(reversed(stack)))