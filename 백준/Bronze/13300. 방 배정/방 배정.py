n, k = map(int, input().split())
students = [[] for _ in range(6)]
for _ in range(n):
  gender, grade = map(int, input().split())
  students[grade-1].append(gender)

answer = 0
for student in students:
  man = student.count(1)
  woman = student.count(0)

  answer += man // k
  answer += man % k
  answer += woman // k
  answer += woman %k

print(answer)