import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var start = 1 // 최소값
    var end = times.max()! * n // 심사하는데 걸리는 최대값
    var mid = 0
    var answer = 0
    
    while start <= end {
        mid = (start + end) / 2
        var sum = 0
        
        for time in times {
            sum += mid / time
        }
        
        if sum < n {
            start = mid + 1
        } else {
            end = mid - 1
            answer = mid
        }
    }
    
    return Int64(answer)
}