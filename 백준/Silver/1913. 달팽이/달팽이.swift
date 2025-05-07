let n = Int(readLine()!)!
let target = Int(readLine()!)!

var array = Array(repeating: Array(repeating: 0, count: n), count: n)
var start_row = 0, end_row = n - 1
var start_col = 0, end_col = n - 1
var num = n * n

while start_row <= end_row && start_col <= end_col {
    // 왼쪽 열 (위 → 아래)
    for i in start_row...end_row {
        array[i][start_col] = num
        num -= 1
    }
    start_col += 1

    // 아래쪽 행 (왼 → 오른쪽)
    if start_col <= end_col {
        for i in start_col...end_col {
            array[end_row][i] = num
            num -= 1
        }
        end_row -= 1
    }

    // 오른쪽 열 (아래 → 위)
    if start_row <= end_row && start_col <= end_col {
        for i in stride(from: end_row, through: start_row, by: -1) {
            array[i][end_col] = num
            num -= 1
        }
        end_col -= 1
    }

    // 위쪽 행 (오른쪽 → 왼쪽)
    if start_row <= end_row && start_col <= end_col {
        for i in stride(from: end_col, through: start_col, by: -1) {
            array[start_row][i] = num
            num -= 1
        }
        start_row += 1
    }
}

// 출력 + 좌표 찾기
var result_row = 0, result_col = 0
for i in 0..<n {
    for j in 0..<n {
        print(array[i][j], terminator: " ")
        if array[i][j] == target {
            result_row = i + 1
            result_col = j + 1
        }
    }
    print()
}
print("\(result_row) \(result_col)")