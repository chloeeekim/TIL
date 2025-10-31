"""

타겟 넘버 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

n개의 음이 아닌 정수들이 주어졌을 때, 정수들의 순서를 변경하지 않고 더하거나 빼서 타겟 넘버를 만드는 방법의 수를 구하는 문제
- 사용할 수 있는 숫자가 담긴 배열 numbers의 길이는 2 이상 20 이하이다
    - 각 숫자는 1 이상 50 이하인 자연수이다
- 타겟 넘버 target은 1 이상 1000 이하인 자연수이다

Example:
- Input : numbers=[1, 1, 1, 1, 1], target=3
- Output : 5

- Input : numbers=[4, 1, 2, 1], target=4
- Output : 2

Note:
주어지는 숫자의 개수가 최대 20개이므로, product를 통해 가능한 모든 경우의 수를 구하여 확인

"""

from itertools import product

def solution(numbers, target):
    prd = product("+-", repeat=len(numbers))

    answer = 0
    for p in prd:
        tsum = 0
        for op, num in zip(p, numbers):
            tsum += num if op == "+" else -num

        answer += 1 if tsum == target else 0

    return answer