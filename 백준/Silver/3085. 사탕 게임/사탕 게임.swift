import Foundation

let n = Int(readLine()!)!
var board:[[String]] = []
var answer = 0

let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]

var nx = 0, ny = 0

for _ in 0..<n {
  board.append(readLine()!.map { String($0) })
}

func findLongline() -> Int {
  var count = 0
  var maxValue = 0

  //행
  for i in 0..<n {
    count = 0
    for j in 0..<n-1 {
      if board[i][j] == board[i][j+1] {
        count += 1
      } else {
        maxValue = max(maxValue, count+1)
        count = 0
      }
    }
    maxValue = max(maxValue, count+1)
  }
  
  
  //열
  for i in 0..<n {
    count = 0
    for j in 0..<n-1 {
      if board[j][i] == board[j+1][i] {
        count += 1
      } else {
        maxValue = max(maxValue, count+1)
        count = 0
      }
    }
    maxValue = max(maxValue, count+1)
  }

  return maxValue
}

// answer = max(answer, findLongline())

for i in 0..<n {
  for j in 0..<n {
    for k in 0..<4 {
      nx = i + dx[k]
      ny = j + dy[k]

      guard 0..<n ~= nx && 0..<n ~= ny else { continue }

      if board[i][j] != board[nx][ny] { // 인접한 사탕이 서로 다르면
        var temp = board[nx][ny]
        board[nx][ny] = board[i][j]
        board[i][j] = temp

        answer = max(answer, findLongline()) // 찾기
        
        temp = board[nx][ny]  // 다시바꾸기
        board[nx][ny] = board[i][j]
        board[i][j] = temp
      }
    }
  }
}

print(answer)