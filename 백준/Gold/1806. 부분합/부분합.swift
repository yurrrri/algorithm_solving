import Foundation

let input = readLine()!.split(separator:" ").map { Int($0)! }
let n = input[0], s = input[1]
let arr = readLine()!.split(separator:" ").map { Int($0)! }

var start = 0, end = 0
var sum = 0, count = 0
var minValue = Int(1e9)

while true {
    if sum >= s {
        minValue = min(minValue, end-start)
        sum -= arr[start]
        start += 1
    } else if end == n {    // 더해야하는데 end를 움직일 수 없으면 break
        break
    } else {
        sum += arr[end]
        end += 1
    }
}

print(minValue == Int(1e9) ? 0:minValue)