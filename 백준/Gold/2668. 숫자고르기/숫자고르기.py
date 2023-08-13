n = int(input())
graph = [[] for _ in range(n+1)]

for a in range(1, n+1):
    b = int(input())
    graph[b].append(a)

visited = [False] * (n+1) # 노드 방문 여부 확인

result = [] # 결과 집합
# route 는 집합
def dfs(node, route):
    global result
  
    route.append(node)
    visited[node] = True
    for i in graph[node]:
        if i not in route:
            dfs(i, route.copy())
        else:# 이미 node가 route에 포함되어있으므로 사이클이 생기는 경우 추가
            result += list(route)
            return

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, [])

result.sort()
print(len(result))
for i in result:
    print(i)