import Foundation

let input = readLine()!.split(separator:" ").map { Int(String($0))! }
let n = input[0], k = input[1]
var arr:[(Int, Int, Int, Int, Int)] = []

for _ in 0..<n {
  let input = readLine()!.split(separator:" ").map { Int(String($0))! }
  arr.append((input[0], input[1], input[2], input[3], 0))
}

for i in 0..<n {
  var seq = 1
  for j in 0..<n {
    if arr[i].1 < arr[j].1 {
      seq += 1
    } else if arr[i].1 == arr[j].1 && arr[i].2 < arr[j].2 {
      seq += 1
    } else if arr[i].1 == arr[j].1 && arr[i].2 == arr[j].2 && arr[i].3 < arr[j].3 {
      seq += 1
    }
  }
  arr[i].4 = seq
}

for i in arr {
  if i.0 == k {
    print(i.4)
  }
}