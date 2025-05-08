import Foundation

func solution(_ board:[[Int]]) -> Int {
    
    let n = board.count     // 행
    let m = board[0].count  // 열
    let dx = [-1, 0, 1, 0]
    let dy = [0, -1, 0, 1]
    var visited = Array(repeating: Array(repeating: Array(repeating: Int.max, count:4), count: m), count: n)
    
    func isValidCoord(_ x: Int, _ y: Int) -> Bool {
        return 0 <= x && x < n && 0 <= y && y < m && board[x][y] == 0
    }
    
    func calculateCost(_ prev: Int, _ current: Int) -> Int {
        if (prev - current) % 2 == 0 {
            return 100
        } else {
            return 600
        }
    }
    
    var q: [(Int, Int, Int)] = []
    
    for i in 0..<4 {
        q.append((0, 0, i))
        visited[0][0][i] = 0
    }
    
    var nx = 0, ny = 0
    
    while !q.isEmpty {
        let (x, y, dir) = q.removeFirst()
        
        for i in 0..<4 {
            nx = x + dx[i]
            ny = y + dy[i]
            
            guard isValidCoord(nx, ny) else { continue }
            let cost = visited[x][y][dir] + calculateCost(dir, i)
            
            if visited[nx][ny][i] > cost {
                visited[nx][ny][i] = cost
                q.append((nx, ny, i))
            }
        }
    }
    
    return visited[n-1][n-1].min()!
}