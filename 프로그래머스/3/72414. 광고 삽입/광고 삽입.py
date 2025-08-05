def transform_time(time):
    hour, minute, second = map(int, time.split(":"))
    
    return 3600 * hour + 60 * minute + second

def reverse_time(time):
    h = time // 3600
    time %= 3600
    m = time // 60
    time %= 60
    s = time
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    play_time = transform_time(play_time)
    adv_time = transform_time(adv_time)
    
    timeline = [0] * (play_time + 2)   # 재생시간 마지막까지 처리 위해 인덱스 범위를 늘림

    # logs의 길이는 최대 360_000이기 때문에 O(n)에 해소하는 알고리즘을 적용해야함
    for log in logs:
        start, end = log.split("-")
        start_sec = transform_time(start)
        end_sec = transform_time(end)
        timeline[start_sec] += 1
        timeline[end_sec] -= 1

    # prefix sum 1: 시각별 시청자 수
    for i in range(1, play_time + 1):
        timeline[i] += timeline[i - 1]

    # prefix sum 2: 시각별 누적 시청시간
    for i in range(1, play_time + 1):
        timeline[i] += timeline[i - 1]

    max_time = 0
    answer = 0
    
    for t in range(play_time - adv_time + 1):
        prefix_sum = timeline[t + adv_time-1] - timeline[t-1]
        if prefix_sum > max_time:
            max_time = prefix_sum
            answer = t

    return reverse_time(answer)