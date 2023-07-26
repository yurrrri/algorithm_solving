struct Score { // 이름 및 점수 저장
    var name: String
    var korean: Int
    var english: Int
    var math: Int
}

let n = Int(readLine()!)!
var students = [Score]()

for _ in 0 ..< n {

	let info = readLine()!.split(separator: " ")
    students.append(Score(name: String(info[0]), korean: Int(info[1])!, 
    english: Int(info[2])!, math: Int(info[3])!)) // n개의 정보 저장
}

students = students.sorted(){ $0.korean == $1.korean ? // 국어 점수가 같다면
	($0.english == $1.english ? // 영어 점수가 같다면
		($0.math == $1.math ? // 수학 점수가 같다면
        $0.name < $1.name: // 이름을 오름차순으로
        $0.math > $1.math) // 영어 점수가 같고, 수학 점수가 다르다면 수학 점수를 오름차순으로
			: $0.english < $1.english) // 국어 점수가 같고, 영어점수가 다르다면 내림차순으로
	: $0.korean > $1.korean} // 국어 점수가 같지 않다면 내림차순으로 정렬한다.

for i in students {
    print(i.name) // 이름만 출력
}