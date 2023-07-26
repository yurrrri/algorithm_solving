var n = Int(readLine()!)!, count = 0, x = 0

for i in 1...Int.max {
    x = i
    while x > 0 { // 각 i마다 1000으로 나누었을 때 나머지가 666이라면 666을 포함하는것임
      // String 형 변환 안하고 666 확인하는 방법
        if x % 1000 == 666 {
          // 오답노트1. 1000으로 나누는 이유
          // 666 -> 나눴을 때 3자리수만 남겨서 확인하기 위함
            count += 1
            break
        }
        x /= 10
    }
    if count == n {
        print(i)
        break
    }
}