
import Foundation

let t = Int(readLine()!)!
var board:[[String]] = []

var fire_visited:[[Int]] = []
var visited:[[Int]] = []

let dx = [0, 0, -1, 1]
let dy = [1, -1, 0, 0]

var nx = 0
var ny = 0

var cur_x = 0
var cur_y = 0

var isSuccessEscape = false

var fire:[(Int, Int)] = []
var w = 0, h = 0

for _ in 0..<t {
  let input = readLine()!.split(separator:" ").map { Int($0)! }
  w = input[0]
  h = input[1]
  
  board = []
  fire_visited = Array(repeating: Array(repeating: -1, count:w), count:h) // 불 번지는 시간
  visited = Array(repeating: Array(repeating: -1, count:w), count:h) // 상근이 가는 시간
  fire = []
  
  for _ in 0..<h {
    board.append(readLine()!.map { String($0) })
  }

  for i in 0..<h {
    for j in 0..<w {
      if board[i][j] == "*" {
        fire.append((i, j))
        fire_visited[i][j] = 0
      } else if board[i][j] == "@" {
        cur_x = i
        cur_y = j
      }
    }
  }

  fire_moving()

  let answer = bfs()
  if answer == -1 {
    print("IMPOSSIBLE")
  } else {
    print(answer)
  }
}

func fire_moving() {
  
  var idx = 0

  while idx < fire.count { // 불 옮기기
    let (x, y) = fire[idx]
    
    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard isValidBound(nx, ny) else { continue }
      
      if board[nx][ny] == "." && fire_visited[nx][ny] == -1 { // 벽이면서 아직 방문하지 않음
        fire_visited[nx][ny] = fire_visited[x][y] + 1
        fire.append((nx, ny))
      }
    }

    idx += 1
  }
}

func bfs() -> Int {
  var q = [(cur_x, cur_y, 0)]
  visited[cur_x][cur_y] = 0
  var idx = 0

  while idx < q.count {
    let (x, y, c) = q[idx]

    for i in 0..<4 {
      nx = x + dx[i]
      ny = y + dy[i]

      guard isValidBound(nx, ny) else { return c+1 } // 범위 벗어나면 바로 거리 출력
      
      if board[nx][ny] == "." && visited[nx][ny] == -1 && (fire_visited[nx][ny] > c+1 || fire_visited[nx][ny] == -1) {
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny, c+1))
      }
    }
    idx += 1
  }
  return -1
}

func isValidBound(_ x:Int, _ y: Int) -> Bool {
  return 0..<h ~= x && 0..<w ~= y
}