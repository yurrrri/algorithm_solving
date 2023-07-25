import Foundation

let input = readLine()!.split(separator:" ").map { Int($0)! }
let m = input[0], n = input[1]   //m: x / n : y
var board:[[Int]] = []
for _ in 0..<m {
  board.append(readLine()!.split(separator:" ").map { Int($0)! })
}

var dp = Array(repeating: Array(repeating: -1, count: n), count:m)

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

var ny = 0, nx = 0

func dfs(_ x: Int, _ y: Int) -> Int {
    if x == m-1 && y == n-1 {
        return 1
    }
    
    if dp[x][y] != -1 {
        return dp[x][y]
    }

    dp[x][y] = 0
    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard 0..<m ~= nx && 0..<n ~= ny else { continue }

      if board[x][y] > board[nx][ny] {
        dp[x][y] += dfs(nx, ny)
      }
    }
    
    return dp[x][y]
}

print(dfs(0, 0))