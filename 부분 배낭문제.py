# items = [[10, 19], [7, 10], [6, 10]]
# weight_limit = 15
items = [[10, 60], [20, 100], [30, 120]]
weight_limit = 50
answer = 0

for item in items:
  item.append(item[1] / item[0])
items.sort(key=lambda x:-x[2])

for item in items:
  if item[0] <= weight_limit:
    weight_limit -= item[0]
    answer += item[1]
  else:
    answer += weight_limit * item[2]  # 이미 배낭을 다 채웠으므로 break
    break

print(f"{answer:.2f}")
