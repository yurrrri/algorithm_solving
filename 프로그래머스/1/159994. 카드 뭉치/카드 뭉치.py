from collections import deque

def solution(cards1, cards2, goal):
    cards1_q = deque(cards1)
    cards2_q = deque(cards2)
    goal_q = deque(goal)
    
    while len(goal_q) > 0:
        if len(cards1_q) > 0 and cards1_q[0] == goal_q[0]:
            cards1_q.popleft()
            goal_q.popleft()
        elif len(cards2_q) > 0 and cards2_q[0] == goal_q[0]:
            cards2_q.popleft()
            goal_q.popleft()
        else:
            return "No"
        
    return "Yes"