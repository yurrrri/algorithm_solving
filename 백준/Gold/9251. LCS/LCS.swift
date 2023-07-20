let str1 = ["0"] + readLine()!.map { $0 }
let str2 = ["0"] + readLine()!.map { $0 }
let n = str1.count
let m = str2.count

var dp = Array(repeating: Array(repeating: 0, count: n), count: m)

for i in 1..<m {
    for j in 1..<n {
        if str2[i] != str1[j] {   // 다르면 이전 값 중 최대값 가져오기
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        } else { // 같으면 + 1
            dp[i][j] = dp[i - 1][j - 1] + 1
        }
    }
}

print(dp[m - 1][n - 1])