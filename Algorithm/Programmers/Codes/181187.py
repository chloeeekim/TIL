"""

두 원 사이의 정수 쌍 : https://school.programmers.co.kr/learn/courses/30/lessons/181187

2차원 직교 좌표계에 중심이 원점인 두 원이 주어졌을 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 구하는 문제
- 두 원은 서로 크기가 다르다
- 원의 반지름을 나타내는 두 정수 r1, r2는 1 이상 1,000,000 이하이며, r1은 r2보다 작다
- 각 원 위의 점도 포함한다

Example:
- Input : r1=2, r2=3
- Output : 20

Note:
각 사분면들은 회전시켰을 때 동일하므로, 1사분면을 기준으로 계산 후 4배로 카운트
정수인 x좌표에 대해 r1과 r2의 y좌표 값을 구하고, 그 범위 안의 정수 개수를 세는 방식

"""

import math

def solution(r1, r2):
    count = 0
    sr1, sr2 = r1 ** 2, r2 ** 2
    for i in range(1, r2 + 1):
        if i < r1:
            yr1 = math.ceil(math.sqrt(sr1 - i ** 2))
        else:
            yr1 = 0

        yr2 = math.floor(math.sqrt(sr2 - i ** 2))
        count += yr2 - yr1 + 1
    return count * 4