from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        if cards1 and cards1[0] == goal[0]:
            goal.popleft()
            cards1.popleft()
        elif cards2 and cards2[0] == goal[0]:
            goal.popleft()
            cards2.popleft()
        else:
            return "No"
    
    return "Yes"