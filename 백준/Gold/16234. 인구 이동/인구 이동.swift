import Foundation

let nlr = readLine()!.split(separator:" ").map { Int(String($0))! }
let n = nlr[0], l = nlr[1], r = nlr[2]

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

var nx = 0
var ny = 0

var board:[[Int]] = []
for _ in 0..<n {
  board.append(readLine()!.split(separator:" ").map { Int(String($0))! })
}

var visited:[[Bool]] = []

func bfs(_ x: Int, _ y: Int) -> Int {
  var q = [(x, y)]
  visited[x][y] = true // visited를 체크하는 이유는 예를들어 50-30 과 30-50 결과가 같으므로 체크해야함
  var union = [(x, y)]

  var sum = board[x][y]
  var idx = 0

  while idx < q.count {
    let (x, y) = q[idx]

    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard 0..<n ~= nx && 0..<n ~= ny && !visited[nx][ny] else { continue }

      if l...r ~= abs(board[nx][ny]-board[x][y]) { // 차이가 l부터 r 이하인 그래프만 탐색해야함 
        visited[nx][ny] = true
        
        union.append((nx, ny))
        q.append((nx, ny))
        sum += board[nx][ny]
      }
    }
    idx += 1
  }

  // 탐색이 끝났으면
  let count = sum / union.count
  for (i, j) in union {
    board[i][j] = count
  }
  return union.count
}

var answer = 0

while true { 
  // while true로 감싸는 이유 : 첫번째 좌표부터 인구이동 여부 확인하는 것을 계속 반복하다가, 더이상 일어나지 않을 때 멈춰야하기 때문
  // 64 ~ 72줄 까지 자체가 처음부터 bfs 돌면서 인구이동 확인하는 부분임
  visited = Array(repeating: Array(repeating: false, count: n), count:n) // visited 초기화한 후 bfs 돈다음 인구이동 여부 확인
  var flag = false
  
  for i in 0..<n {
    for j in 0..<n {
      if !visited[i][j] {
        if bfs(i, j) > 1 {
          flag = true
        }
      }
    }
  }

  if !flag { break }
  answer += 1
}

print(answer)