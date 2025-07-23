from collections import deque

n, w, l = map(int, input().split())   # n: 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
truck_weights = deque(list(map(int, input().split())))
bridge = deque([0] * w)
answer = 0
bridge_weight = 0

while bridge:
    answer += 1         # 1초 더하기
    bridge_weight -= bridge.popleft()   # 1초가 지날때마다 다리를 건너는 트럭이 다리를 지남
    
    if truck_weights:
        if bridge_weight + truck_weights[0] <= l: 
            truck = truck_weights.popleft() 
            bridge_weight += truck 
            bridge.append(truck) 
        else: 
            bridge.append(0)
    
print(answer)