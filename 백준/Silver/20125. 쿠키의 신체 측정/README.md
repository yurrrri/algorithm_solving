# [Silver IV] 쿠키의 신체 측정 - 20125 

[문제 링크](https://www.acmicpc.net/problem/20125) 

### 성능 요약

메모리: 149928 KB, 시간: 164 ms

### 분류

구현

### 제출 일자

2025년 7월 31일 14:41:54

### 문제 설명

<p style="user-select: auto !important;">쿠키런은 데브시스터즈에서 제작한 모바일 러닝 액션 게임이다. 마녀의 오븐에서 탈출한 쿠키들과 함께 모험을 떠나는 게임으로, 점프와 슬라이드 2가지 버튼만으로 손쉽게 플레이할 수 있는 것이 특징이다.</p>

<p style="user-select: auto !important;">연세대학교를 졸업한 김강산 선배님이 데브시스터즈에 취직하면서 주변 사람들에게 쿠키런을 전파시켰다. 하지만 게임을 전파하던 중에 쿠키들에게 신체적으로 이상이 생기는 것을 발견하였다. 팔, 다리 길이가 임의적으로 변한 것이다. 때문에 긴급하게 각 쿠키들의 신체들을 측정하려고 한다.</p>

<p style="user-select: auto !important;">쿠키들은 신체를 측정하기 위해서 한 변의 길이가 <em style="user-select: auto !important;">N</em>인 정사각형 판 위에 누워있으며, 어느 신체 부위도 판 밖으로 벗어나지 않는다. 판의 <em style="user-select: auto !important;">x</em>번째 행, <em style="user-select: auto !important;">y</em>번째 열에 위치한 곳을 (<em style="user-select: auto !important;">x</em>, <em style="user-select: auto !important;">y</em>)로 지칭한다. 판의 맨 왼쪽 위 칸을 (1, 1), 오른쪽 아래 칸을 (<em style="user-select: auto !important;">N</em>, <em style="user-select: auto !important;">N</em>)으로 나타낼 수 있다.</p>

<p style="text-align: center; user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/94002737-4414-4de5-8d1f-d80da455de7d/-/preview/" style="user-select: auto !important;"></p>

<p style="user-select: auto !important;">그림과 같이 쿠키의 신체는 머리, 심장, 허리, 그리고 좌우 팔, 다리로 구성되어 있다. 그림에서 빨간 곳으로 칠해진 부분이 심장이다. 머리는 심장 바로 윗 칸에 1칸 크기로 있다. 왼쪽 팔은 심장 바로 왼쪽에 붙어있고 왼쪽으로 뻗어 있으며, 오른쪽 팔은 심장 바로 오른쪽에 붙어있고 오른쪽으로 뻗어있다. 허리는 심장의 바로 아래 쪽에 붙어있고 아래 쪽으로 뻗어 있다. 왼쪽 다리는 허리의 왼쪽 아래에, 오른쪽 다리는 허리의 오른쪽 아래에 바로 붙어있고, 각 다리들은 전부 아래쪽으로 뻗어 있다. 각 신체 부위들은 절대로 끊겨있지 않으며 굽혀진 곳도 없다. 또한, 허리, 팔, 다리의 길이는 1 이상이며, 너비는 무조건 1이다.</p>

<p style="user-select: auto !important;">쿠키의 신체가 주어졌을 때 심장의 위치와 팔, 다리, 허리의 길이를 구하여라.</p>

### 입력 

 <p style="user-select: auto !important;">다음과 같이 입력이 주어진다.</p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; user-select: auto !important;"><em style="user-select: auto !important;">N</em><br style="user-select: auto !important;">
<em style="user-select: auto !important;">a<sub style="user-select: auto !important;">1,1</sub></em> . . . <em style="user-select: auto !important;">a<sub style="user-select: auto !important;">1,N</sub></em><br style="user-select: auto !important;">
. . . . . .<br style="user-select: auto !important;">
<em style="user-select: auto !important;">a<sub style="user-select: auto !important;">N,1</sub></em> . . . <em style="user-select: auto !important;">a<sub style="user-select: auto !important;">N,N</sub></em></div>

### 출력 

 <p style="user-select: auto !important;">첫 번째 줄에는 심장이 위치한 행의 번호 <em style="user-select: auto !important;">x</em>와 열의 번호 <em style="user-select: auto !important;">y</em>를 공백으로 구분해서 출력한다.</p>

<p style="user-select: auto !important;">두 번째 줄에는 각각 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이를 공백으로 구분해서 출력하여라.</p>

