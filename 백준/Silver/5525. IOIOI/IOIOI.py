n = int(input())
m = int(input())
letters = input()
leter = "I" + "OI" * n
answer = 0

for i in range(m-(2*n+1)+1):
  candi = letters[i:i+len(leter)]
  if leter in candi:
    answer += 1

print(answer)