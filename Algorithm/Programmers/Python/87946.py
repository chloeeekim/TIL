"""

피로도 : https://school.programmers.co.kr/learn/courses/30/lessons/87946

유저의 현재 피로도와 던전별 피로도 정보가 주어졌을 때, 유저가 탐험할 수 있는 최대 던전 수를 구하는 문제
- 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 존재한다
- 각 던전은 한 번씩만 탐험할 수 있다
- 유저의 현재 피로도 k는 1 이상 5,000 이하인 자연수이다
- 던전별 피로도가 담긴 2차원 배열 dungeons의 길이는 1 이상 8 이하이다
    - dungeons의 가로(열) 길이는 2이다
    - dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"]이다
    - "최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같다
    - "최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수이다
    - 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있다

Example:
- Input : k=80, dungeons=[[80,20],[50,40],[30,10]]
- Output : 3
- 1 -> 3 -> 2번째 순서로 던전을 탐험할 수 있다

Note:
순열을 이용한 완전 탐색으로 해결
던전의 최대 개수가 8개이므로, permutation으로 가능한 모든 경우의 수를 구해도 문제 없다

"""

from itertools import permutations

def solution(k, dungeons):
    length = len(dungeons)
    perm = permutations(dungeons, length)

    answer = 0
    for p in perm:
        temp = k
        count = 0
        for need, use in p:
            if temp >= need:
                temp -= use
                count += 1
            else:
                break
        answer = max(answer, count)

    return answer