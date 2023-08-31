import Foundation

// func radixChange(_ t: Int, _ n: Int) -> String {
//     var t = t
//     var nums:[String] = []
//     let alpha = ["A", "B", "C", "D", "E", "F"]
//     var remains = 0
//     if t == 0 {
//         return String(t)
//     }
    
//     while t > 0 {
//         remains = t%n
//         t /= n
        
//         if n == 16 && remains >= 10 { // 16진수인 경우에 10~15는 알파벳으로 표시
//             nums.append(alpha[remains-10])
//         } else {
//             nums.append(String(remains))
//         }
//     }
    
//     return Array(nums.reversed()).joined()
// }

func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    // n: 진법, t: 미리 구할 숫자의 개수, m: 게임 참여 인원, p: 정답이 말해야하는 순서
    var arr:[String] = []
    for i in 0..<t*m {  // 게임 참여 인원 vs 튜브가 말해야하는 숫자 개수 곱함
        arr += String(i, radix:n).uppercased().map { String($0) }
    }
    var result = ""

    for i in stride(from: p-1, to: t*m, by:m) {
        result += arr[i]
    }
    
    return result
}