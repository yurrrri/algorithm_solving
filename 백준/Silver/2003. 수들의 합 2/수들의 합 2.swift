let input = readLine()!.split(separator:" ").map { Int(String($0))! }
let n = input[0], m = input[1]
let arr = readLine()!.split(separator:" ").map { Int(String($0))! }

var start = 0, end = 0
var sum = 0, count = 0

while true {
    if sum >= m {
        sum -= arr[start]
        start += 1
    } else if end == n {    // 더해야하는데 end를 움직일 수 없으면 break
        break
    } else {
        sum += arr[end]
        end += 1
    }
    if sum == m { count += 1 }
}

print(count)