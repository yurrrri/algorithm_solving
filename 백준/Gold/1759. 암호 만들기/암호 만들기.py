l, c = map(int, input().split())
arr = sorted(list(input().split()))
visited = [False] * c

def count_moeum_zaeum(str):
  moeums = ["a", "e", "i", "o", "u"]
  moeum = 0
  zaeum = 0
  
  for s in str:
    if s in moeums:
      moeum += 1
    else:
      zaeum += 1

  return moeum >= 1 and zaeum >= 2

def backtracking(str, idx):
  if count_moeum_zaeum(str) and len(str) == l:
    print(str)
    return

  for i in range(idx, c):
    if not visited[i]:
      visited[i] = True
      backtracking(str + arr[i], i)
      visited[i] = False

backtracking("", 0)