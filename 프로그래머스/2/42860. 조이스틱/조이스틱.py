def solution(name):
    answer = 0
    n = len(name)

    for ch in name:
        if (ch != 'A'):
            min_up_down = min(ord(ch) - ord('A'), 26 + ord('A') - ord(ch))
            answer += min_up_down

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer