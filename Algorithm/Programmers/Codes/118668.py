"""

코딩 테스트 공부 : https://school.programmers.co.kr/learn/courses/30/lessons/118668

알고력, 코딩력, 문제의 정보가 주어졌을 때, 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하는 문제
- 특정 문제를 풀기 위해서는 문제가 요구하는 일정 이상의 알고력과 코딩력이 필요하다
- 알고력과 코딩력을 높이기 위한 방법은 다음과 같다
    - 알고리즘 공부: 알고력 1을 높이기 위해 1의 시간이 필요하다
    - 코딩 공부: 코딩력 1을 높이기 위해 1의 시간이 필요하다
    - 문제 해결: 현재 풀 수 있는 문제 중 하나를 풀어 알고력과 코딩력을 높인다
    - 문제 하나를 푸는 데는 문제가 요구하는 시간이 필요하며, 같은 문제를 여러 번 푸는 것이 가능하다
- 모든 문제들을 한 번 이상씩 풀 필요는 없다
- problems의 원소는 [alp_req, cop_req, alp_rwd, cop_rwd, cost]의 형태로 이루어져 있다
    - 각각 문제를 푸는데 필요한 알고력과 코딩력, 문제를 풀었을 때 증가하는 알고력과 코딩력, 문제를 푸는데 필요한 시간을 의미한다

Example:
- Input : alp=10, cop=10, problems=[[10,15,2,1,2],[20,20,3,3,4]]
- Output : 15
- 코딩 공부 5번: 코딩력 5 증가 / 시간 5 소요 -> 알고력 10, 코딩력 15
- 1번 문제 해결 5번: 알고력 10 증가 / 코딩력 5 증가 / 시간 10 소요 -> 알고력 20, 코딩력 20

- Input : alp=0, cop=0, problems=[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
- Output : 13

Note:
dp로 해결
problems의 alp_req, cop_req 중 max가 도달해야 하는 알고력과 코딩력
현재의 alp, cop가 요구사항보다 높은 경우를 고려

"""

import sys

def solution(alp, cop, problems):
    al_max, co_max = max(p[0] for p in problems), max(p[1] for p in problems)
    al_max, co_max = max(alp, al_max), max(cop, co_max)

    if alp >= al_max and cop >= co_max:
        return 0

    dp = [[sys.maxsize] * (co_max + 1) for _ in range(al_max + 1)]
    dp[alp][cop] = 0

    for i in range(alp, al_max + 1):
        for j in range(cop, co_max + 1):
            if i < al_max:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < co_max:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for pr in problems:
                if i >= pr[0] and j >= pr[1]:
                    nalp = min(al_max, i + pr[2])
                    ncop = min(co_max, j + pr[3])
                    dp[nalp][ncop] = min(dp[nalp][ncop], dp[i][j] + pr[4])

    return dp[al_max][co_max]