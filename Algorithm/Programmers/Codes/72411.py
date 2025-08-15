"""

메뉴 리뉴얼 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

손님들이 주문한 단품메뉴들의 조합이 주어졌을 때, 가장 많이 함께 주문한 단품메뉴 조합을 구하는 문제
- 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성되며, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 포함한다
- orders 배열의 원소는 크기가 2 이상 10 이하인 문자열이며, 각 문자열은 A ~ Z의 알파벳 대문자로 이루어진다
- orders의 원소에는 같은 알파벳이 중복해서 들어있지 않다
- course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있으며, 중복된 값이 존재하지 않는다
- 오름차순으로 정렬된 각 코스요리 메뉴의 구성을 오름차순으로 정렬하여 배열에 담아 리턴한다
- orders와 course 매개변수는 리턴하는 배열의 길이가 1 이상이 되도록 주어진다

Example:
- Input : orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], course=[2, 3, 4]
- Output : ["AC", "ACDE", "BCFG", "CDE"]

- Input : orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], course=[2, 3, 5]
- Output : ["ACD", "AD", "ADE", "CD", "XYZ"]

- Input : orders=["XYZ", "XWY", "WXA"], course=[2, 3, 4]
- Output : ["WX", "XY"]
- 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 포함되므로, 요리 3개와 4개로 구성된 코스요리는 추가하지 않는다

Note:
itertools의 combinations를 이용하여 모든 조합을 구하는 방식

"""

import itertools
from collections import defaultdict

def solution(orders, course):
    order_count = defaultdict(int)
    max_count = [0] * len(course)

    for order in orders:
        for i, c in enumerate(course):
            combination = list(itertools.combinations(sorted(order), c))
            for comb in combination:
                order_count[comb] += 1
                max_count[i] = max(max_count[i], order_count[comb])

    result = []
    for i, c in enumerate(course):
        result += [k for k, v in order_count.items() if v > 1 and len(k) == c and v >= max_count[i]]

    return sorted([''.join(x) for x in result])