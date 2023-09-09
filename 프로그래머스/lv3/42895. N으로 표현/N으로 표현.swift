// 방법 1 -> DFS 돌리기
import Foundation

var answer = 9

func dfs(_ n: Int, _ number: Int, _ count: Int, _ currentNumber: Int) {
    if count >= 9 { return }
    if currentNumber == number {
        answer = min(answer, count)
        return
    }
    var temp = 0
    for i in 1...9 {
        temp = temp * 10 + n // 5, 55, 555, ...
        dfs(n, number, count + i, currentNumber + temp)
        dfs(n, number, count + i, currentNumber - temp)
        dfs(n, number, count + i, currentNumber * temp)
        dfs(n, number, count + i, currentNumber / temp)
    }
}

func solution(_ n:Int, _ number:Int) -> Int {
    dfs(n, number, 0, 0)
    if answer > 8 { return -1 }
    return answer
}
    
// 방법 2: DP 활용하기
// func solution(_ n: Int, _ number: Int) -> Int {
//     // n을 사용한 횟수에 따른 각 연산의 결과를 저장할 집합 리스트
//     // 집합을 사용하는 이유 -> 중복을 제거하기 위함
//     var dp: [Set<Int>] = Array(repeating: [], count: 9)

//     var temp = 0
//     for i in 1..<9 {
//         temp = 10*temp + n  //5, 55, 555....
//         dp[i].insert(temp) //각 자리수에 맞는 집합에 길이가 i인, n을 연결한 temp를 넣어줌 (길이가 1이면 첫번째 집합, 길이가 2이면 두번째 집합...)
        
//         for j in 1..<i { // i이전까지,
//             for k in dp[j] { //i가 5라면 그 이전의 개수일때의 연산 조합으로 number를 만들 수 있는지 봐야함
//                 // 1, 2, 3, 4...
//                 for l in dp[i-j]{  // 4, 3, 2, 1... 이렇게 각각 더하면 총 i번 사용한 연산을 만들 수 있게됨
//                     dp[i].insert(k + l)
//                     dp[i].insert(k - l)
//                     dp[i].insert(k * l)
//                     if l != 0 && k != 0 {
//                         dp[i].insert(k/l)
//                     }
//                 }
//             }
//         }
        
//         if dp[i].contains(number) {  // 1, 2, 3, 4...를 돌때마다 number가 있는지 확인하고, 바로 return을 해주어도 최소값을 보장하므로 바로 return해줌
//             return i
//         }
//     }
//     return -1 //위에서 결과를 찾지 못한 경우 -1
// }