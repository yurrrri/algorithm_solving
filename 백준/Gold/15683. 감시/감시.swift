import Foundation

let readline = readLine()!.split(separator:" ").map { Int($0)! }
let (n, m) = (readline[0], readline[1])
var board:[[Int]] = []
var cctvs:[(Int, Int)] = []  // cctv의 좌표를 저장하는 배열
let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]
// 우 하 좌 상 순서 offset 배열
var answer = Int.max

for i in 0..<n {
  board.append(readLine()!.split(separator:" ").map { Int($0)! })
  for j in 0..<m {
    if Array(1...5).contains(board[i][j]) {
      cctvs.append((i, j))
    }
  }
}

func isValidCoord(_ x: Int, _ y: Int) -> Bool {    // 유효한 좌표인지를 판단하는 함수
  return 0 <= x && x < n && 0 <= y && y < m
}

func setMonitor(_ cctv_x: Int, _ cctv_y: Int, _ dir: Int) {
  var x = cctv_x
  var y = cctv_y
  let dir = dir % 4   // dir가 인덱스 범위를 벗어나면 다시 인덱스 범위에 속하도록 만들어주기 위해 계산하는 식

  while true {  // 벽을 마주칠때까지 반복
    x += dx[dir]
    y += dy[dir]

    if !isValidCoord(x, y) || board[x][y] == 6 { break }
    if board2[x][y] == 0 {
      board2[x][y] = -1
    }
  }
}

var board2 = board   // 매번 케이스에 따라서 갯수가 달라지므로 복사에 사용할 배열
for i in 0..<Int(pow(4.0, Double(cctvs.count))) {     // 4^cctv의 갯수가 모든 경우의 수
  var brute = i
  board2 = board

  for j in 0..<cctvs.count {
    let dir = brute % 4
    brute /= 4
    let (x,y) = cctvs[j]
    let type = board[x][y]

        switch type {
        case 1:
            setMonitor(x, y, dir)
        case 2:
            setMonitor(x, y, dir)
            setMonitor(x, y, dir + 2)
        case 3:
            setMonitor(x, y, dir)
            setMonitor(x, y, dir + 1)
        case 4:
            setMonitor(x, y, dir)
            setMonitor(x, y, dir + 1)
            setMonitor(x, y, dir + 2)
        case 5:
            setMonitor(x, y, dir)
            setMonitor(x, y, dir + 1)
            setMonitor(x, y, dir + 2)
            setMonitor(x, y, dir + 3)
        default:
            break
        }
    }

    var blindCount = 0
    for i in 0..<n {
        for j in 0..<m {
            if board2[i][j] == 0 {
                blindCount += 1
            }
        }
    }

    answer = min(answer, blindCount)
}

print(answer)