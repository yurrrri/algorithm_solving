import Foundation

let nk = readLine()!.split(separator:" ").map { Int($0)! }
let n = nk[0], k = nk[1]

var dp = Array(repeating: Array(repeating:0, count: k+1), count:n+1)
var arr:[(Int, Int)] = [(0, 0)]
for _ in 0..<n {
  let input = readLine()!.split(separator:" ").map { Int($0)! }
  arr.append((input[0], input[1]))
}

for i in 1...n {
  for j in 1...k {
    let (w, v) = arr[i]

    if j >= w { // j가 현재 담으려는 물건의 무게보다 크거나 같으면
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

    } else {
      dp[i][j] = dp[i-1][j] // 이전 값 그대로 가져옴
    }
  }
}

print(dp[n][k])