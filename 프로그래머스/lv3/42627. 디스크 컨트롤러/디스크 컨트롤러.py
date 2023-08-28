import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):  # 작업이 남아있는 동안 아래 로직을 실행
        for j in jobs:
            if start < j[0] <= now: # 이전 작업의 요청 시간보다 크면서 현재 시간보다 작거나 같은 작업 추가
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우, 작업처리
            cur = heapq.heappop(heap)
            start = now
            now += cur[0] # 작업을 끝낸 현재 시간 --> now + 작업시간
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1 # 작업을 처리했으므로 i+1
        else: # 처리할 작업이 없는 경우에 시간이 흘러가므로 now + 1
            now += 1
                
    return answer // len(jobs)