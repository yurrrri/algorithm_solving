import heapq

def solution(jobs):
    answer = 0
    heap = []
    start, now = -1, 0  # 각 작업의 작업 시작 시간, 작업이 끝나면서 현재 시간
    i = 0 # 작업의 현재 인덱스
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:  # 만약 처리안한 작업중에 이전 작업 요청시간보다 크면서 현재 시간보다  작거나 같은 작업이 있다면, 힙 작업열에 추가
                heapq.heappush(heap, (job[1], job[0]))
                
        if heap: # 만약 처리할 작업이 있다면
            time, req = heapq.heappop(heap)  # 차례대로 소요시간, 요청시간
            start = now  # 작업 시작 시간을 현재 시간으로 갱신
            now += time   # 현재 시간 갱신
            answer += now - req # 현재에서 작업 요청시간을 뺀 것을 더하면 요청부터 종료까지의 소요시간을 더하는것임
            i += 1 # 작업을 완료했으므로 인덱스 증가
        else:   # 처리할 작업이 없다면, 시간은 흘러가므로 now + 1
            now += 1
                
    return answer // len(jobs)