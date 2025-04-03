import Foundation

let n = Int(readLine()!)!
var board:[[Int]] = []
var visited = Array(repeating: Array(repeating: 0, count: n), count: n)
var count = 0
var answer = 0

for _ in 0..<n {
  board.append(readLine()!.split(separator:" ").map { Int($0)! })
}

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

var nx = 0, ny = 0

var maxHeight = board.flatMap { $0 }.max()!

// func dfs(_ x: Int, _ y: Int, _ height: Int) {
//   for i in 0..<4 {
//     nx = x + dx[i]
//     ny = y + dy[i]

    // guard 0..<n ~= nx && 0..<n ~= ny && visited[nx][ny] == 0 else { continue }

//     if board[nx][ny] > height {
//       visited[nx][ny] = 1   // 안전 영역일 경우에 방문처리하고
//       dfs(nx, ny, height)   // 인접한 영역으로 들어가서 탐색함
//     }
//   }
// }
func bfs(_ x: Int, _ y: Int, _ height: Int) {
  var q = [(x, y)]
  var idx = 0

  while idx < q.count {
    let (x, y) = q[idx]

    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard 0..<n ~= nx && 0..<n ~= ny && visited[nx][ny] == 0 else { continue }

      if board[nx][ny] > height {
        q.append((nx, ny))
        visited[nx][ny] = 1
      }
    }
    idx += 1
  }
}

for i in 0...maxHeight {  // 아무지역도 물에 안잠길수도 있다 -> 0부터 시작
  visited = Array(repeating: Array(repeating: 0, count: n), count: n)
  count = 0

  for j in 0..<n {
    for k in 0..<n {
      if board[j][k] > i && visited[j][k] == 0 { // 방문하지 않았으면서, 안전영역을 탐색할 시점일 경우 (board[j][k] > i)
        count += 1  
        visited[j][k] = 1
        bfs(j, k, i)   // 안전영역에 모두 방문처리를 함으로써, 방문하지 않은 영역만 방문해서 갯수를 세게 함
      }
    }
  }

  answer = max(answer, count)
}

print(answer)