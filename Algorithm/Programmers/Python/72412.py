"""

순위 검색 : https://school.programmers.co.kr/learn/courses/30/lessons/72412

지원자들의 정보가 주어졌을 때, 특정 조건에 해당하는 지원자가 몇 명인지 구하는 문제
- [조건]을 만족하는 사람 중 테스트 점수를 X점 이상 받은 사람을 구한다
- info의 원소는 "개발언어 직군 경력 소울푸드 점수" 형태이며, 각 단어는 공백 문자 하나로 구분된다
    - 개발언어는 cpp, java, python 중 하나이다
    - 직군은 backend, frontend 중 하나이다
    - 경력은 junior, senior 중 하나이다
    - 소울푸드는 chicken, pizza 중 하나이다
    - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수이다
- query의 원소는 "[조건] X" 형태이며, 각 단어는 공백 문자 하나로 구분된다
    - [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형태의 문자열이다
    - 언어, 직군, 경력, 소울푸드는 - 표시가 가능하며, - 표시된 조건은 고려하지 않는다

Example:
- Input : info=
[
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
], query=
[
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]
- Output : [1,1,1,1,2,4]

Note:
itertools의 combinations를 사용하여 각 지원자의 조건과 -의 조합을 생성
생성된 조합을 공백 하나를 포함하여 합친 문자열을 key로 사용하여 hash 하는 방식
효율성 테스트가 있기 때문에 성능을 위해 검색 시에 bisect_left 사용

"""

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    info_hash = defaultdict(list)

    for i in info:
        sinfo = i.split()
        score = sinfo[-1]

        for j in range(5):
            combs = combinations(range(4), j)

            for comb in combs:
                key = sinfo[:4]
                for elem in comb:
                    key[elem] = "-"
                info_hash[" ".join(key)].append(int(score))
    for item in info_hash:
        info_hash[item].sort()

    result = []
    for q in query:
        squery = q.replace(" and", "").split()
        target = int(squery[-1])

        key = " ".join(squery[:4])
        score_list = info_hash[key]
        if not score_list:
            result.append(0)
            continue

        start = bisect_left(score_list, target)
        result.append(len(score_list) - start)

    return result