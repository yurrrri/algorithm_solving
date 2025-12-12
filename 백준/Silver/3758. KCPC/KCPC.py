from collections import defaultdict

t = int(input())
for _ in range(t):
  # 팀의 갯수, 문제 갯수, 팀의 id, 로그의 갯수
  n, k, t, m = map(int, input().split())
  dic = {x: [0, 0, 0] for x in range(1, n+1)}
  score = {x: [0] * (k+1) for x in range(1, n+1)}
  
  for time in range(m):   # 제출 시간
    # 팀 id, 문제 번호, 획득한 점수
    i, j, s = map(int, input().split())
    dic[i][1] += 1
    dic[i][2] = time
    score[i][j] = max(score[i][j], s)

  for x in range(1, n+1):
    dic[x][0] = sum(score[x])

  result = sorted(dic.items(), key=lambda x:(-x[1][0], x[1][1], x[1][2]))
  for idx, arr in enumerate(result):
    if arr[0] == t:
      print(idx+1)