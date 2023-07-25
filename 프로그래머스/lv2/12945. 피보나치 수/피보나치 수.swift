func solution(_ n:Int) -> Int {
    var dp = Array(repeating: 0, count:100001)
    dp[0] = 0
    dp[1] = 1
    
    for i in 2...n {
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    }
    return dp[n]
}