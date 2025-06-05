n = int(input())
arr = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
answer_lst = []

def backtracking(_sum, p, m, mt, d, depth):
  if depth == n:
    answer_lst.append(_sum)
    return

  if p < plus:
    backtracking(_sum + arr[depth], p+1, m, mt, d, depth+1)

  if m < minus:
    backtracking(_sum - arr[depth], p, m+1, mt, d, depth+1)

  if mt < multi:
    backtracking(_sum * arr[depth], p, m, mt+1, d, depth+1)

  if d < divide:
    if _sum < 0 and arr[depth] > 0:
      temp = _sum * -1
      temp //= arr[depth]
      temp *= -1
      backtracking(temp, p, m, mt, d+1, depth+1)
    else:
      backtracking(_sum // arr[depth], p, m, mt, d+1, depth+1)

backtracking(arr[0], 0, 0, 0, 0, 1)

print(max(answer_lst))
print(min(answer_lst))