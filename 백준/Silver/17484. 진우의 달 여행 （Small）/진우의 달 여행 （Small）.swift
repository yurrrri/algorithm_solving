import Foundation

let input = readLine()!.split(separator:" ").map { Int($0)! }
let n = input[0], m = input[1]

let dy = [-1, 0, 1] // 왼쪽, 아래, 오른쪽
var nx = 0, ny = 0
var answer = Int(1e9)
var arr:[[Int]] = []

for _ in 0..<n {
  arr.append(readLine()!.split(separator:" ").map { Int($0)! })
}

func dfs(_ sum: Int, _ x: Int, _ y: Int, _ dir: Int) {
  if x == n {
    answer = min(answer, sum)
    return
  }

  for j in 0..<3 {
    if dir == j { continue }
    ny = y + dy[j]

    guard 0..<m ~= ny else { continue }
    dfs(sum + arr[x][ny], x+1, ny, j)
  }
}

for i in 0..<m {  // i 0, 1, 2, 3 순 시작
  dfs(0, 0, i, -1)
}

print(answer)