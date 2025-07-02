def solution(name):
    answer = 0
    n = len(name)

    for ch in name:       # 1)
        if (ch != 'A'):
            min_up_down = min(ord(ch) - ord('A'), 26 + ord('A') - ord(ch))
            answer += min_up_down
            
    move = 21          # 2)
    for left in range(n):
        idx = left + 1
        while (idx < n) and (name[idx] == 'A'):
            idx += 1
            
        right = n - idx
        distance = min(left, right)
        move = min(move, left + right + distance)

    answer += move
    
    return answer