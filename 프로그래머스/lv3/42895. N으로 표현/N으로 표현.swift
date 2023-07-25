import Foundation

func solution(_ n:Int, _ number:Int) -> Int {
    var answer = 9
    var temp = 0
    
    func dfs(_ result: Int, _ count: Int) {
        //오답노트 2. 아래를 안쓰면 core dumped 에러가 뜨는이유?
        //1. recursive 오류일수도 있고,
        //2. 제한을 안걸어주면 result값이 계속 커지는데 이게 정수의 범위를 넘어서서 발생하는 현상일수도 있음
        if count >= 9 {
            return
        }
        
        if result == number {
            answer = min(answer, count)
            return
        }
        
        //오답노트 1. 재귀를 들어갈 떄마다 temp를 0으로 초기화하는 이유?
        // 그 다음 연산으로 들어갈 때마다 다시 5, 55, 555... 순으로 사칙연산 경우의 수를 따져줘야하니, 기존의 값을 쓰는것이 아닌 다시 처음부터 시작해야함
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