"""

후보키 : https://school.programmers.co.kr/learn/courses/30/lessons/42890

릴레이션을 나타내는 2차원 배열이 주어졌을 때, 유일성과 최소성을 만족하는 후보키의 개수를 구하는 문제
- 유일성이란 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 함을 의미한다
- 최소성이란 유일성을 가진 키를 구성하는 속성 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다
- relation은 2차원 문자열 배열이다
    - relation의 컬럼의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다
    - relation의 로우의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다
    - relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다
    - relation의 모든 튜플은 유일하게 식별 가능하다 (중복되는 튜플은 존재하지 않는다)

Example:
- Input : relation=
[
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]
- Output : 2
- 0번 속성, [1번 속성, 2번 속성]이 후보키가 된다

Note:
itertools의 combinations를 사용하여 가능한 모든 조합을 구하는 방식으로 해결
해당 조합에 의해 유일성이 보장된다면, 기존 후보키들과 비교하여 subset 여부 확인

"""

from itertools import combinations

def solution(relation):
    row, column = len(relation), len(relation[0])
    idxs = [i for i in range(column)]
    keys = []
    for i in range(1, column + 1):
        combination = combinations(idxs, i)
        for comb in combination:
            selected = [tuple(row[i] for i in comb) for row in relation]
            if len(set(selected)) == row:
                for k in keys:
                    if set(k).issubset(comb):
                        break
                else:
                    keys.append(comb)
    return len(keys)