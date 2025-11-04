from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]  
        while progresses and progresses[0] >= 100:  # 앞의 기능이 진도가 100% 이상일때까지 같이 popleft함 (하루에 같이 배포하기 위해)
            count += 1
            progresses.popleft()
            speeds.popleft()    # speeds를 함께 popleft하는 이유는, 위 10번째 라인에서 progresses만 pop하게 되면 인덱스가 안맞아서 각 공정에 맞는 스피드로 계산할 수가 없게된다.
        if count:
            answer.append(count)
    return answer