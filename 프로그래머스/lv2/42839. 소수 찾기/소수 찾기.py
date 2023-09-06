from itertools import permutations

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)

    combi = set()
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers, i))
        for j in arr:
            combi.add(''.join(j))

    answer = set()
    for c in combi:
        if isPrime(int(c)):
            answer.add(int(c))

    return len(answer)