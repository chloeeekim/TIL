"""

점 찍기 : https://school.programmers.co.kr/learn/courses/30/lessons/140107

두 양의 정수 k, d가 주어졌을 때, 총 몇 개의 점이 찍히는지 구하는 문제
- 점은 다음과 같은 방식으로 찍는다
    - 원점 (0, 0)으로부터 x축 방향으로 a * k (a = 0, 1, 2, 3, ...), y축 방향으로 b * k (b = 0, 1, 2, 3, ...)만큼 떨어진 위치에 점을 찍는다
    - 원점과 거리가 d를 넘는 위치에는 점을 찍지 않는다
- k는 1 이상 1,000,000 이하의 정수이다
- 원점과의 거리를 나타내는 정수 d는 1 이상 1,000,000 이하이다

Example:
- Input : k=2, d=4
- Output : 6
- (0, 0), (0, 2), (0, 4), (2, 0), (2, 2), (4, 0) 위치에 점을 찍는다

- Input : k=1, d=5
- Output : 26

Note:
원점으로부터의 거리가 d 이하인 범위는 반지름이 d인 원의 내부가 된다
x축 좌표에 대해 원의 y 좌표를 구한 다음, 내부에 점을 찍을 수 있는 갯수를 카운트

"""

import math

def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        y = math.sqrt(d ** 2 - x ** 2)
        answer += math.floor(y) // k + 1

    return answer