n = int(input())
arr = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
max_ans = -1e11
min_ans = 1e11

def backtracking(_sum, p, m, mt, d, depth):
  global max_ans
  global min_ans
  
  if depth == n:
    if max_ans < _sum:
      max_ans = _sum
    if min_ans > _sum:
      min_ans = _sum
    return

  if p < plus:
    backtracking(_sum + arr[depth], p+1, m, mt, d, depth+1)

  if m < minus:
    backtracking(_sum - arr[depth], p, m+1, mt, d, depth+1)

  if mt < multi:
    backtracking(_sum * arr[depth], p, m, mt+1, d, depth+1)

  if d < divide:
    if _sum < 0:
      backtracking(-(-_sum // arr[depth]), p, m, mt, d+1, depth+1)
    else:
      backtracking(_sum // arr[depth], p, m, mt, d+1, depth+1)

backtracking(arr[0], 0, 0, 0, 0, 1)

print(max_ans)
print(min_ans)