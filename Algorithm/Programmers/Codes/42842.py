"""

카펫 : https://school.programmers.co.kr/learn/courses/30/lessons/42842

카펫의 갈색 격자의 수와 노란색 격자의 수가 주어졌을 때, 카펫의 가로, 세로 크기를 구하는 문제
- 카펫은 중앙에는 노란색으로 칠해져 있고, 테두리 1줄은 갈색으로 칠해져 있다
- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수이다
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수이다
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다
- 카펫의 가로, 세로 크기를 순서대로 배열에 담아 리턴한다

Example:
- Input : brown=10, yellow=2
- Output : [4, 3]

- Input : brown=8, yellow=1
- Output : [3, 3]

- Input : brown=24, yellow=24
- Output : [8, 6]

Note:
yellow의 가로, 세로로 i, j가 가능할 때,
brown은 i * 2 + j * 2 + 4여야 한다

"""

import math

def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            ywidth = yellow // i
            if (i * 2) + (ywidth * 2) + 4 == brown:
                return [ywidth + 2, i + 2]

    return [0, 0]