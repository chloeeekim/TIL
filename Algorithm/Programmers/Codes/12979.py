"""

기지국 설치 : https://school.programmers.co.kr/learn/courses/30/lessons/12979

기존 기지국들의 위치와 변경되는 기지국의 전파 도달 거리가 주어졌을 때, 모든 아파트에 전파를 전달하기 위해 증설해야 하는 기지국의 최소 개수를 구하는 문제
- 전파 도달 거리가 W일 때, 기지국이 설치된 아파트를 기준으로 양쪽으로 W만큼 전파를 전달할 수 있다
- 아파트의 개수 N은 200,000,000 이하의 자연수이다
- 현재 기지국이 설치된 아파트들의 번호가 담긴 1차원 배열 stations의 크기는 10,000 이하의 자연수이다
    - stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수이다
- 전파 도달 거리 W는 10,000 이하의 자연수이다

Example:
- Input : N=11, stations=[4, 11], W=1
- Output : 3

- Input : N=16, stations=[9], W=2
- Output : 3

Note:
기지국의 전파가 닿지 않는 영역에 추가할 수 있는 최소한의 기지국의 개수를 구해 더하는 방식

"""

import math

def solution(n, stations, w):
    start = 0
    res = 0
    width = 2 * w + 1
    for station in stations:
        empty = station - w - start - 1
        if empty > 0:
            res += math.ceil(empty / width)
        start = station + w
    if n - start > 0:
        res += math.ceil((n - start) / width)
    return res