from collections import deque

topni = [[0]] # 껍데기 0 하나 넣어두기
answer = 0

for _ in range(4):
	topni.append(list(map(int, input()))) # 붙어있는 정수 리스트
#0: N극, 1: S극
k = int(input()) # 회전 횟수

def countScore(one, two, three, four):
	sum = 0
	if one == 1:
		sum += 1
	if two == 1:
		sum += 2
	if three == 1:
		sum += 4
	if four == 1:
		sum += 8
	return sum

#1번: 2번 인덱스
#2번: 2, 6
#3번: 2, 6
#4번: 6

for _ in range(k):
	num, dir = map(int, input().split()) # 회전시킨 톱니바퀴 번호, 방
#1: 시계방향 -1: 반시계방향
	if num == 1:
		save1 = topni[2][2]
		save2 = topni[3][2]
		
		if topni[1][2] != topni[2][6]:
			temp = deque(topni[2])
			temp.rotate(-dir)
			topni[2] = list(temp)

			if save1 != topni[3][6]:
				temp = deque(topni[3])
				temp.rotate(dir)
				topni[3] = list(temp)

				if save2 != topni[4][6]:
					temp = deque(topni[4])
					temp.rotate(-dir)
					topni[4] = list(temp)

		temp = deque(topni[1])
		temp.rotate(dir)
		topni[1] = list(temp)

	elif num == 2:
		save1 = topni[3][2]
		
		if topni[2][2] != topni[3][6]:
			temp = deque(topni[3])
			temp.rotate(-dir)
			topni[3] = list(temp)

			if save1 != topni[4][6]:
					temp = deque(topni[4])
					temp.rotate(dir)
					topni[4] = list(temp)

		if topni[2][6] != topni[1][2]:
			temp = deque(topni[1])
			temp.rotate(-dir)
			topni[1] = list(temp)

		temp = deque(topni[2])
		temp.rotate(dir)
		topni[2] = list(temp)
	elif num == 3:
		save1 = topni[2][6]
		
		if topni[3][2] != topni[4][6]:
			temp = deque(topni[4])
			temp.rotate(-dir)
			topni[4] = list(temp)

		if topni[3][6] != topni[2][2]:
			temp = deque(topni[2])
			temp.rotate(-dir)
			topni[2] = list(temp)

			if save1 != topni[1][2]:
				temp = deque(topni[1])
				temp.rotate(dir)
				topni[1] = list(temp)

		temp = deque(topni[3])
		temp.rotate(dir)
		topni[3] = list(temp)

	elif num == 4:
		save1 = topni[3][6]
		save2 = topni[2][6]
		
		if topni[4][6] != topni[3][2]:
			temp = deque(topni[3])
			temp.rotate(-dir)
			topni[3] = list(temp)

			if save1 != topni[2][2]:
				temp = deque(topni[2])
				temp.rotate(dir)
				topni[2] = list(temp)

				if save2 != topni[1][2]:
					temp = deque(topni[1])
					temp.rotate(-dir)
					topni[1] = list(temp)

		temp = deque(topni[4])
		temp.rotate(dir)
		topni[4] = list(temp)

print(countScore(topni[1][0], topni[2][0], topni[3][0], topni[4][0]))