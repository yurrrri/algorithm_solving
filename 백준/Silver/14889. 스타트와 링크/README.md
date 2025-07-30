# [Silver I] 스타트와 링크 - 14889 

[문제 링크](https://www.acmicpc.net/problem/14889) 

### 성능 요약

메모리: 79516 KB, 시간: 232 ms

### 분류

브루트포스 알고리즘, 백트래킹

### 제출 일자

2023년 6월 13일 17:40:28

### 문제 설명

<p style="user-select: auto !important;">오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.</p>

<p style="user-select: auto !important;">BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 S<sub style="user-select: auto !important;">ij</sub>는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 S<sub style="user-select: auto !important;">ij</sub>의 합이다. S<sub style="user-select: auto !important;">ij</sub>는 S<sub style="user-select: auto !important;">ji</sub>와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S<sub style="user-select: auto !important;">ij</sub>와 S<sub style="user-select: auto !important;">ji</sub>이다.</p>

<p style="user-select: auto !important;">N=4이고, S가 아래와 같은 경우를 살펴보자.</p>

<table class="table table-bordered" style="width: 20%; user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">i\j</th>
			<th style="user-select: auto !important;">1</th>
			<th style="user-select: auto !important;">2</th>
			<th style="user-select: auto !important;">3</th>
			<th style="user-select: auto !important;">4</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">1</th>
			<td style="user-select: auto !important;"> </td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">3</td>
		</tr>
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">2</th>
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;"> </td>
			<td style="user-select: auto !important;">5</td>
			<td style="user-select: auto !important;">6</td>
		</tr>
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">3</th>
			<td style="user-select: auto !important;">7</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;"> </td>
			<td style="user-select: auto !important;">2</td>
		</tr>
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">4</th>
			<td style="user-select: auto !important;">3</td>
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;">5</td>
			<td style="user-select: auto !important;"> </td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">스타트 팀: S<sub style="user-select: auto !important;">12</sub> + S<sub style="user-select: auto !important;">21</sub> = 1 + 4 = 5</li>
	<li style="user-select: auto !important;">링크 팀: S<sub style="user-select: auto !important;">34</sub> + S<sub style="user-select: auto !important;">43</sub> = 2 + 5 = 7</li>
</ul>

<p style="user-select: auto !important;">1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">스타트 팀: S<sub style="user-select: auto !important;">13</sub> + S<sub style="user-select: auto !important;">31</sub> = 2 + 7 = 9</li>
	<li style="user-select: auto !important;">링크 팀: S<sub style="user-select: auto !important;">24</sub> + S<sub style="user-select: auto !important;">42</sub> = 6 + 4 = 10</li>
</ul>

<p style="user-select: auto !important;">축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.</p>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 S<sub style="user-select: auto !important;">ij</sub> 이다. S<sub style="user-select: auto !important;">ii</sub>는 항상 0이고, 나머지 S<sub style="user-select: auto !important;">ij</sub>는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.</p>

### 출력 

 <p style="user-select: auto !important;">첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.</p>

