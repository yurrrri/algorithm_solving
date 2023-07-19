import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var w = 0, h = 0
    let sum = brown + yellow
    for i in 1...sum {
        if sum%i == 0 { // 나누어 떨어지는 수 중에
            w = sum/i   // 가로 세로를 구한다음
            h = i       // 공식이 해당되는지 확인
            if (w-2) * (h-2) == yellow {
                break
            }
        }
    }
    return [w, h]
}