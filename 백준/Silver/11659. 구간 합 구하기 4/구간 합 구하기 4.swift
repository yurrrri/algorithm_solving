import Foundation

var input = readLine()!.split(separator:" ").map { Int($0)! }
let n = input[0], m = input[1] //m번 반복
var nums = readLine()!.split(separator:" ").map { Int($0)! }

if n == 1 {
  print(nums.first!)
  exit(0)
}

var area:[(Int, Int)] = []
for _ in 0..<m {
  input = readLine()!.split(separator:" ").map { Int($0)! }
  // 인덱스로 접근하기 위해 각각 -1
  area.append((input[0]-1, input[1]-1))
}

// 누적합 구하기
for i in 1..<nums.count {
  nums[i] += nums[i-1]
}

for (x, y) in area {
  if x-1 < 0 {
    print(nums[y])
  } else {
    print(nums[y] - nums[x-1])
  }
}