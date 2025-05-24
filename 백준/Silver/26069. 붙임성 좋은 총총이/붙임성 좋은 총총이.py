n = int(input())
dancing_person = set(["ChongChong"])
for _ in range(n):
  a, b = input().split()
  if a in dancing_person or b in dancing_person:
    dancing_person.add(a)
    dancing_person.add(b)

print(len(dancing_person))