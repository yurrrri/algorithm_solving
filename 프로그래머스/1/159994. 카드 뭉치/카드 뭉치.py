from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:     # goal의 원소가 남아있을동안
        if cards1 and cards1[0] == goal[0]:    
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:      # 앞의 순서가 맞지 않으면 만들지 못하므로 바로 return No
            return "No"
        
    return "Yes"