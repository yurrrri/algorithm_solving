import Foundation

func solution(_ n:Int, _ number:Int) -> Int {
    var answer = 9
    var temp = 0
    
    func dfs(_ result: Int, _ count: Int) {
        if count >= 9 {
            return
        }
        
        if result == number {
            answer = min(answer, count)
            return
        }
        
        var temp = 0
        for i in 1...9 {
            temp = 10*temp + n // 5, 55, 555, 55555.....
            dfs(result + temp, count+i)
            dfs(result - temp, count+i)
            dfs(result * temp, count+i)
            dfs(result / temp, count+i)
        }
    }
    
    dfs(0, 0)
    return answer >= 9 ? -1 : answer
}