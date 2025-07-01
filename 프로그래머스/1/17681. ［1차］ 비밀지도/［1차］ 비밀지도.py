def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.zfill(n)       # 길이가 모자란 부분은 공백으로 채워줘야하므로 zfill을 통해 0으로 채운다음 아래에서 " "로 바꿈
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer