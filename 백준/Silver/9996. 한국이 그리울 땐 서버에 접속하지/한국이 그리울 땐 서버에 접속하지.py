n = int(input())
expression = input().split("*")
start = expression[0]
end = expression[1]

for _ in range(n):
  word = input()
  if len(word) >= len(start) + len(end) and word.startswith(start) and word.endswith(end):
    print("DA")
  else:
    print("NE")