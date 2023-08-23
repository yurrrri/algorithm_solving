import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var truck_weights = truck_weights
    var passing = Array(repeating:0, count:bridge_length)  // 다리를 건너고있는 트럭을 bridge_length 길이 배열 만큼 생성
    var answer = 0
    var bridge_weight = 0 // 다리 위의 무게
    
    // 다리에는 최대 bridge_length 만큼만 트럭이 올라갈 수 있으며, weight 이하의 무게를 견딜 수 있음
    while !passing.isEmpty {
        //카운트를 하고
        answer += 1
        //다리를 다 건넌 트럭의 무게를 뺴줌
        bridge_weight -= passing.removeFirst()
        
        //대기중인 트럭이 있다면
        if !truck_weights.isEmpty {
            if bridge_weight + truck_weights.first! <= weight { // 대기중인 트럭 다리 건너게 하기
                passing.append(truck_weights.first!)
                bridge_weight += truck_weights.removeFirst()  // 무게 추가
            } else { // 못보낸다면 0 추가하기
                passing.append(0)
            }
        } 
    }
    return answer
}