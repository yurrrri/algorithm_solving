n = int(input().rstrip())
balls = input().rstrip()
cnt = []

# R을 오른쪽
red_right = balls.rstrip('R')
cnt.append(red_right.count('R'))

# B를 오른쪽
blue_right = balls.rstrip('B')
cnt.append(blue_right.count('B'))

# R을 왼쪽
red_left = balls.lstrip('R')
cnt.append(red_left.count('R'))

# B를 왼쪽
blue_left = balls.lstrip('B')
cnt.append(blue_left.count('B'))

print(min(cnt))