import Foundation

let n = Int(readLine()!)! //짝수 -> 절반으로 나눠야함
var board:[[Int]] = []

for _ in 0..<n {
  board.append(readLine()!.split(separator:" ").map { Int($0)! })
}

// 완탐 or 백트래킹? -
var visited = Array(repeating: false, count:n)
var minValue = Int(1e9)
var star = 0, link = 0

func backtracking(_ depth: Int, _ idx: Int) {
  if depth == n/2 {  // n/2로 좁힌 이유 -> 어차피 절반 뽑으면 나머지 절반은 자동 구성이기 때문
    star = 0
    link = 0
    
    for i in 0..<n {
      for j in 0..<n {
        if visited[i] && visited[j] {
          star += board[i][j]
        }

        if !visited[i] && !visited[j] {
          link += board[i][j]
        }
      }
    }

    minValue = min(minValue, abs(star-link))   // i 와 j - j와 i가 겹치므로 /2를 해줘야함
    
    return
  }

  for i in idx..<n {  // 순열이 아니라 조합이라고 생각하면 13이나 31이나 같으므로 idx부터 시작
    if !visited[i] {
      visited[i] = true  // visited를 체크하는 이유는 나중에 계산할 때 팀을 나눠서 계산해야하기 때문임
      backtracking(depth+1, i+1) // 한명 인원 더 선발하기
      visited[i] = false
    }
  }
}

backtracking(0, 0)
print(minValue)