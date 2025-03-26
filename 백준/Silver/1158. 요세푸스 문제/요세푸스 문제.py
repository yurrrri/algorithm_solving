from collections import deque

N, k = map(int, input().split())

queue = deque(range(1, N+1))
answer = []

while len(queue) > 0:
  for _ in range(k-1):
    queue.append(queue.popleft())

  answer.append(str(queue.popleft()))

print("<" + ", ".join(answer) + ">")