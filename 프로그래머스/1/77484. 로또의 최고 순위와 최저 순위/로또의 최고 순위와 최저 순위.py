def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    
    for w in win_nums:
        if w in lottos:
            count += 1
    
    return [rank[lottos.count(0) + count], rank[count]]