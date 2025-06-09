from collections import Counter
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
  word = input().rstrip()
  if len(word) < m:
    continue

  arr.append(word)

counter = Counter(arr)
arr = set(arr)
arr = sorted(arr, key=lambda x:(-counter[x], -len(x), x))
# 1. 자주나오는 단어 --> counter value값 내림차순
# 2. 해당 단어의 길수록 앞에 배치 --> len값 기준 내림차순
# 3. 알파벳 사전 순으로 앞에 있는 단어 --> 사전 순 오름차순
print("\n".join(arr))
