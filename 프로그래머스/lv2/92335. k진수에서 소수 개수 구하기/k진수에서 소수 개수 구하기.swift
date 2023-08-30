import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    var splited = String(n, radix: k).split(separator:"0").filter { $0 != "1" }
    var arr = splited.map { Int(String($0))! }
    var answer = 0
    
    for e in arr {
        var flag = false
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