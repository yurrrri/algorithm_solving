from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = deque([0] * bridge_length)     # [0]*bridge_length 을 덱으로 변환
    truck_weights = deque(truck_weights)    # 리스트를 덱으로 변환
    currentWeight = 0
    
    while bridge:
        answer += 1
        currentWeight -= bridge.popleft()
        
        if truck_weights:
            if currentWeight + truck_weights[0] <= weight:
                currentWeight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else: 
                bridge.append(0)
                
    return answer