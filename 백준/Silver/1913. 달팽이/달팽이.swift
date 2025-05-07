import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!

var arr = Array(repeating: Array(repeating: 0, count: n), count: n)

// 하우상좌
let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

var dir = 0
var num = n * n
var x = 0, y = 0

var targetX = 0
var targetY = 0

while num > 0 {
    arr[x][y] = num
    if num == m {
        targetX = x + 1
        targetY = y + 1
    }

    var nx = x + dx[dir]
    var ny = y + dy[dir]

    if !(0 <= nx && nx < n && 0 <= ny && ny < n && arr[nx][ny] == 0) {
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    }

    x = nx
    y = ny
    num -= 1
}

// 출력
for row in arr {
    print(row.map { String($0) }.joined(separator: " "))
}
print("\(targetX) \(targetY)")