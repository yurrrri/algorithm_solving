import sys
sys.setrecursionlimit(10**6)

s = input()
t = input()

def canStoT(str):
  if str == s:
    print(1)
    exit()

  if len(str) <= len(s):
    return

  if str[-1] == "A":
    tmp = str[:-1]
    canStoT(tmp)

  if str[0] == "B":
    tmp = str[::-1][:-1]
    canStoT(tmp)

canStoT(t)
print(0)