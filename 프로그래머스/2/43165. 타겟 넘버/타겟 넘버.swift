import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var answer = 0
    
    func dfs(_ sum: Int, _ depth: Int) {
        if depth == numbers.count {  // 모든 정수들을 활용해야하므로 depth가 numbers의 길이와 같아야하며, 이를 넘어서면 안되므로 return 처리함
            if sum == target {     // 이때 target과 같으면 저장
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