import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var truck_weights = truck_weights //큐
    var passing = Array(repeating:0, count:bridge_length)
    var answer = 0
    var bridge_weight = 0
    
    // 다리에는 최대 bridge_length 만큼만 트럭이 올라갈 수 있으며, weight 이하의 무게를 견딜 수 있음
    while !truck_weights.isEmpty || bridge_weight != 0{
        //카운트를 하고
        answer += 1
        //다리를 다 건넌 트럭의 무게를 뺴줌(트럭이 아니라면 0을 뺌
        bridge_weight -= passing.removeFirst()
        
        //대기중인 트럭이 있다면
        if !truck_weights.isEmpty{
            //트럭이 올라갈 수 있는 무게라면
            if bridge_weight + truck_weights[0] <= weight {
                //트럭의 무게를 더해주고
                bridge_weight += truck_weights[0]
                //트럭을 올려주고
                passing.append(truck_weights[0])
                //첫 번째를 삭제해줌
                truck_weights.removeFirst()
            //트럭이 올라갈 수 없다면
            }else{
                //한 칸 전진
                passing.append(0)
            }
        }
    }
    return answer
}