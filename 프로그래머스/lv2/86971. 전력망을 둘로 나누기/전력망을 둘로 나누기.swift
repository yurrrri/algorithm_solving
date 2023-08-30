import Foundation

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    var graph: [[Int]] = Array(repeating: [], count:n+1)
    var answer = Int(1e9)
    var visited:[Bool] = []
    
    for wire in wires {
        let a = wire[0]
        let b = wire[1]
        graph[a].append(b)
        graph[b].append(a)
    }
        
    func bfs(_ start: Int, _ link: [[Bool]]) -> Int {
        visited[start] = true
        var q = [start]
        var count = 1
        
        while !q.isEmpty {
            var x = q.removeFirst()
            
            for i in graph[x] {
                if !visited[i] && link[x][i] {
                    visited[i] = true
                    count += 1
                    q.append(i)
                }
            }
        }
        
        return count
    }
    
    var link = Array(repeating: Array(repeating: true, count:n+1), count:n+1)
    
    for wire in wires {
        let a = wire[0]
        let b = wire[1]
        
        visited = Array(repeating: false, count: n+1)
        link[a][b] = false
        let result1 = bfs(a, link)
        let result2 = bfs(b, link)
        link[a][b] = true
        
        answer = min(answer, abs(result1 - result2))
    }
    
    return answer
}