var input = readLine()!.split(separator:" ").map { Int(String($0))!}
let N = input[0] //세로 크기
let M = input[1] //가로 크기

input = readLine()!.split(separator:" ").map { Int(String($0))!}
var x = input[0]
var y = input[1]
var direction = input[2] //방향
var board:[[Int]] = []

for _ in 0..<N {
  board.append(readLine()!.split(separator:" ").map { Int(String($0))!})
}

let dx = [-1, 0, 1, 0]
let dy = [0, 1, 0, -1]

func rotate() {
  direction -= 1
  if direction == -1 {
    direction = 3
  }
}

var nx = 0 //이동하는 좌표
var ny = 0

board[x][y] = 2
var count = 1
var rotation_count = 0

while true {

    rotate()
  
    nx = x+dx[direction]
    ny = y+dy[direction]
    
    if board[nx][ny] == 0 {
        x = nx //전진
        y = ny
  
        board[nx][ny] = 2 //청소

        count += 1
        rotation_count = 0
    }
    else {
      rotation_count += 1
    }

    if rotation_count == 4 {
      rotation_count = 0
      nx = x - dx[direction]
      ny = y - dy[direction]

      if board[nx][ny] != 1 {
        x = nx
        y = ny
      }
      else{
        break
      }
    }
}

print(count)