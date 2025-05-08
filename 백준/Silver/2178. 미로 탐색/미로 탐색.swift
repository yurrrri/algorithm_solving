let input = readLine()!.split(separator:" ").map { Int($0)! }
let (n, m) = (input[0], input[1])
var board:[[Int]] = []
var visited = Array(repeating: Array(repeating: 0, count: m), count: n)
let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]
var nx = 0, ny = 0

for _ in 0..<n {
  board.append(readLine()!.map { Int(String($0))! })
}

var q = [(0, 0)]
visited[0][0] = 1

while !q.isEmpty {
  let (x, y) = q.removeFirst()

  for i in 0..<4 {
    nx = x + dx[i]
    ny = y + dy[i]

    guard 0 <= nx && nx < n && 0 <= ny && ny < m && visited[nx][ny] == 0 && board[nx][ny] == 1 else { continue }

    visited[nx][ny] = visited[x][y] + 1
    q.append((nx, ny))
  }
}

print(visited[n-1][m-1])