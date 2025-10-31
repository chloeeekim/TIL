"""

소수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

종이 조각에 적힌 숫자들이 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 구하는 문제
- 종이 조각에는 한 자리 숫자가 적혀 있다
- 종이 조각에 적힌 숫자가 적힌 문자열 number의 길이는 1 이상 7 이하이다
    - numbers는 0~9까지의 숫자만으로 이루어져 있다
    - "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져 있다는 의미이다

Example:
- Input : numbers="17"
- Output : 3
- 7, 17, 71을 만들 수 있다

- Input : numbers="011"
- Output : 2
- 11, 101을 만들 수 있다

Note:
permutations를 사용하여 만들 수 있는 모든 경우의 수를 확인
set을 사용하여 중복을 제거

"""

from itertools import permutations
import math

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    perm = []
    for i in range(1, len(numbers) + 1):
        perm.extend(permutations(numbers, i))

    answer = set()
    for p in list(perm):
        num = int("".join(p))
        if isPrime(num):
            answer.add(num)

    return len(answer)