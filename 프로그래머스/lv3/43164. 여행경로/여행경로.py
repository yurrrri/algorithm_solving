#1. 시간 오래걸리는 풀이
# def solution(tickets):
#     answer = []
#     visited = [False] * len(tickets)

#     def dfs(arr, airport):
#         if False not in visited: #모두 방문했다면 (모든 경로를 들렀다면)
#             answer.append(arr)
#             return
#         for i in range(len(tickets)):
#             if not visited[i]:
#                 if tickets[i][0] == airport:
#                     visited[i] = True
#                     dfs(arr + [tickets[i][1]], tickets[i][1])
#                     visited[i] = False

#     dfs(["ICN"], "ICN")
#     answer.sort()

#     return answer[0]

from collections import defaultdict

def dfs(graph, path, visit):
    if path:
        to = path[-1]
        if graph[to]: path.append(graph[to].pop(0))
        else: visit.append(path.pop())
        dfs(graph, path, visit)
    
    return visit[::-1]

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in tickets: graph[a].append(b)
    for key in graph.keys(): graph[key].sort()
    
    return dfs(graph, ["ICN"], [])