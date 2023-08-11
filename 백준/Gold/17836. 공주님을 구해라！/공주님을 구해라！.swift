let input = readLine()!.split(separator:" ").map { Int(String($0))! }
let n = input[0], m = input[1], t = input[2] //제한시간
var board:[[Int]] = []
var visited = Array(repeating: Array(repeating: 0, count:m), count: n)

for _ in 0..<n {
  board.append(readLine()!.split(separator:" ").map { Int(String($0))! })
}

var nx = 0
var ny = 0
var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]
var usedGramTime = 10001

func bfs() -> Int {
  visited[0][0] = 1
  var q = [(0, 0)]

  while !q.isEmpty {
    let (x, y) = q.removeFirst()

    if x == n-1 && y == m-1 {
      return min(visited[x][y]-1, usedGramTime)
    }

    if board[x][y] == 2 {
      usedGramTime = n-1-x + m-1-y + visited[x][y]-1
    }
    
    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard 0..<n ~= nx && 0..<m ~= ny else { continue } 

      if visited[nx][ny] == 0 && board[nx][ny] != 1 {
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
      }
    }
  }

  return usedGramTime
}

let result = bfs()

if result > t {
  print("Fail")
} else {
  print(result)
}