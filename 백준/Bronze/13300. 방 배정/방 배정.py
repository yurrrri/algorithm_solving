import math

n, k = map(int, input().split())
students = [[] for _ in range(6)]
for _ in range(n):
  gender, grade = map(int, input().split())
  students[grade-1].append(gender)

answer = 0

for student in students:
  man = student.count(1)
  woman = student.count(0)

  answer += math.ceil(man / k) + math.ceil(woman / k)

print(answer)