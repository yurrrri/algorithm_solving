def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준 정렬
    prev_camera = -30001  # 이전에 설치한 카메라 위치
    answer = 0

    for start, end in routes:
        if start > prev_camera:
            answer += 1          # 새 카메라 필요
            prev_camera = end    # 현재 차량의 진출 지점에 카메라 설치

    return answer