import Foundation

// func radixChange(_ n: Int, _ radix: Int) -> String {
//     var nums:[String] = []
//     var n = n
    
//     while n > 0 {
//         var remain = n%radix
//         n /= radix
        
//         nums.append(String(remain))  // 나머지를 차례대로 배열에 넣은 후
//     }
    
//     return Array(nums.reversed()).joined()  // 거꾸로 뒤집어서 합친 문자열 반환
// }

func solution(_ n:Int, _ k:Int) -> Int {
    var splited = String(n, radix: k).split(separator:"0").filter { $0 != "1" }
    /* 여기서 0을 기준으로 separate를 하는 이유
    
    */
    var arr = splited.map { Int(String($0))! }
    var answer = 0
    
    for e in arr {
        var flag = false
        // var visited = Array(repeating: true, count: e+1)
        // for i in 2...Int(sqrt(Double(e))) + 1 {
        //     if visited[i] {
        //         var j = 2
        //         while (i*j) <= e {
        //             visited[i*j] = false
        //             j += 1
        //         }
        //     }
        // }
        // if visited[e] {
        //     answer += 1
        // }
        for i in 2...Int(sqrt(Double(e))) + 1 {
            if e%i == 0 && e != i {
                flag = true
                break
            }
        }
        if !flag {
            answer += 1
        }
    }
    
    return answer
}