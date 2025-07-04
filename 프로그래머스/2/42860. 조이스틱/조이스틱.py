def solution(name):
    answer = 0
    n = len(name)

    for ch in name:       # 1) A에서 해당 알파벳까지 바꾸는 데 드는 총 최소 횟수 (각 알파벳마다 위 버튼, 아래 버튼을 누른 횟수를 합쳐서 최소값을 비교함)
        if (ch != 'A'):
            min_up_down = min(ord(ch) - ord('A'), 26 + ord('A') - ord(ch))
            answer += min_up_down
            
    move = 21          # 2) 좌우로 이동하여 알파벳을 바꾸는 횟수의 최소값
    for left in range(n):
        idx = left + 1        # 일단 쭉 오른쪽 커서를 통해 직진한다고 가정하고, 왼쪽 커서로 이동하는 횟수와 비교한다.
        while (idx < n) and (name[idx] == 'A'):
            idx += 1
            
        right = n - idx      # 해당 위치로 이동하기 위해 왼쪽 커서로 이동하는 경우
        distance = min(left, right)      # 왼쪽 혹은 오른쪽으로 갔다가, 그 반대방향으로 다시 꺾어서 오는 경우
        move = min(move, left + right + distance)

    answer += move
    
    return answer