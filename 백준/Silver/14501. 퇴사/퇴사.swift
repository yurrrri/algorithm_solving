import Foundation

let n = Int(readLine()!)!
var arr:[(Int, Int)] = [(0, 0)] // 껍데기

var dp = Array(repeating: 0, count:n+1) // 최대 수익 DP 테이블, i: 기간

for _ in 1...n {
  let input = readLine()!.split(separator:" ").map { Int($0)! }
  arr.append((input[0], input[1])) // 상담을 하는데 필요한 기간, 이익
}

for i in 1...n {
  dp[i] = max(dp[i-1], dp[i]) // 자기 날짜의 기존 수익 값과 이전까지 일했을 때의 값이 곧 그날까지 얻을 수 있는 수익의 최대값
  let dur = i + arr[i].0 - 1
  if dur <= n { // 퇴사 일 이후를 넘기지 않는지 확인
    dp[dur] = max(dp[dur], dp[i-1] + arr[i].1)
  }
}

print(dp.max()!)