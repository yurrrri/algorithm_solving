from collections import deque

visited = [0] * 101 #이동 횟수를 기록할 배열
board = [0] * 101 #뱀과 사다리의 정보를 저장할 배열 (값이 0이 아니라면 이동할 수 있는 사다리나 뱀이 있다는 뜻)

n, m = map(int, input().split())
for _ in range(n+m):
	x, y = map(int, input().split())
	board[x] = y

q = deque([1])

while q:
	x = q.popleft()

	for i in range(1, 7):
		nx = x + i
		if nx > 100: break

		# 뱀이나 사다리가 없다면 원래 주사위 굴린대로 이동
		whereWeGo = nx if board[nx] == 0 else board[nx]

		if visited[whereWeGo] == 0:
			visited[whereWeGo] = visited[x] + 1
			q.append(whereWeGo)  #탐색

print(visited[100])