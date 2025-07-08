def solution(lottos, win_nums):
    answer = [7, 7]
    count = 0
    
    for w in win_nums:
        if w in lottos:
            count += 1
            
    answer[1] -= count
    answer[0] -= count
    
    have_to_fill = len(win_nums) - count
    if have_to_fill >= lottos.count(0):
        answer[0] -= lottos.count(0)
        
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6
    
    return answer