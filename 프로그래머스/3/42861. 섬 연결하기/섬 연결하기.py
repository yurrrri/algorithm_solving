def solution(n, costs):
    
    parent = [i for i in range(n)]   # 처음에는 다 자기 자신이 부모 노드임
    rank = [0] * n   # 유니온파인드의 기준이 될 rank 배열
    costs.sort(key=lambda x:x[2])
        
    def find(i):
        if parent[i] == i:
            return i
        
        parent[i] = find(parent[i])
        return parent[i]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
    
    answer = 0
    edges = 0
    
    for node1, node2, cost in costs:
        if edges == n-1:
            break
            
        x = find(node1)
        y = find(node2)
        
        if x != y:    # 사이클 순환을 방지하면서 유니온 하기 위함
            union(x, y)
            
            answer += cost
            edges += 1
            
    return answer