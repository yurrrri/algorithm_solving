import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    /*
    1) 수의 범위가 엄청 크다 -> 이분탐색이라고 가정
    2) 탐색 범위를 고민 -> 보통 return하는 값을 기준으로 start, end, mid 지점을 잡는다 생각하고 한번 더 적절한지 고민
    3) 최소, 최대값 설정 (탐색할 처음 지점과 끝 지점)
    4) while 문으로 돌면서 최적값을 확인하며, 최적해를 구해야하는 경우에는 result에 값이 될만한 후보를 저장하고 있어야함
    */
    var start = 1 // 최소값
    var end = times.max()! * n // 심사하는데 걸리는 최대값
    var mid = 0
    var answer = 0
    
    while start <= end {
        mid = (start + end) / 2
        var people = 0
        
        for time in times {
            people += mid / time
            if people >= n { // n명을 넘어가면 더이상 계산할 필요없으므로 break
                break
            }
        }
        
        if people < n {
            start = mid + 1
        } else {
            end = mid - 1
            answer = mid  // 기준이 될 수 있는 값이니까 후보 저장
        }
    }
    
    return Int64(answer)
}