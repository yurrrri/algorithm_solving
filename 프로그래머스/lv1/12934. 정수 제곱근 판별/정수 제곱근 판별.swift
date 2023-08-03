import Foundation

func solution(_ n:Int64) -> Int64 {
    if sqrt(Double(n)) == floor(sqrt(Double(n))) {
        return Int64(pow(sqrt(Double(n))+1, 2))
    } else {
        return -1
    }
}