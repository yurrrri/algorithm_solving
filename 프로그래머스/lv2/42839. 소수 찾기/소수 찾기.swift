import Foundation

func isPrime(_ num: Int) -> Bool {
    if (num < 4) {
        return num <= 1 ? false : true
    }
    for i in 2...Int(sqrt(Double(num))) {
        if (num % i == 0) { return false }
    }
    return true
}

func solution(_ numbers:String) -> Int {
    var result:Set<Int> = []
    var visited = Array(repeating: false, count: numbers.count)
    
    func permutation(_ nums:[String], _ targetNum:Int) {
        func permute(_ arr:[String]) {
            if arr.count == targetNum {
                let num = Int(arr.joined())!
                if isPrime(num) { 
                    result.insert(num)
                }
                return
            }

            for i in 0..<nums.count {
                if !visited[i] {
                    visited[i] = true
                    permute(arr + [nums[i]])
                    visited[i] = false
                }
            }
        }

        permute([])
    }
    
    for i in 1...numbers.count { // 일부 숫자만 조합하여 소수 판단하는 케이스도 넣어야하므로, 1개만 골랐을 때...모든 수 다 골랐을 때의 케이스를 모두 판단해주어야함
        visited = Array(repeating: false, count: numbers.count)
        
        permutation(numbers.map { String($0) }, i)
    }
    
    return result.count
}