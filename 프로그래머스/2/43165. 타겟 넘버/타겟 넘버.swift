import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var answer = 0
    
    func dfs(_ sum: Int, _ depth: Int) {
        if depth == numbers.count {
            if sum == target {
                answer += 1
            }
            return
        }
        
        dfs(sum + numbers[depth], depth+1)
        dfs(sum - numbers[depth], depth+1)
    }
    
    dfs(0, 0)
    
    return answer
}