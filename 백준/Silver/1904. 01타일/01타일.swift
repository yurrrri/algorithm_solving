import Foundation

let n = Int(readLine()!)!
var dp = Array(repeating: 0, count: n+1)

if n == 1 {
  print(1)
  exit(0)
} else if n == 2 {
  print(2)
  exit(0)
} else {
  dp[1] = 1
  dp[2] = 2

  for i in 3...n {
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
  }
}

print(dp[n])