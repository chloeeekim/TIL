"""

실패율 : https://school.programmers.co.kr/learn/courses/30/lessons/42889

사용자가 현재 도전 중인 스테이지의 번호 리스트가 주어졌을 때, 실패율이 높은 스테이지부터 내림차순으로 구하는 문제
- 실패율은 스테이지에 도달했으나 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수이다
- stages의 원소는 1 이상 N+1 이하의 자연수로, 각 숫자는 사용자가 현재 도전 중인 스테이지의 번호이다
- stages가 N+1인 경우, 마지막 스테이지(N번째 스테이지)까지 클리어한 사용자를 의미한다
- 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 정렬한다
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다

Example:
- Input : N=5, stages=[2, 1, 2, 6, 2, 4, 3, 3]
- Output : [3,4,2,1,5]

- Input : N=4, stages=[4,4,4,4,4]
- Output : 	[4,1,2,3]
- 4번 스테이지의 실패율은 1이며, 나머지 스테이지의 실패율은 0이므로 작은 번호부터 정렬

Note:
collections의 Counter를 사용하여 동일한 스테이지에 있는 사용자들을 한꺼번에 처리
해당 스테이지를 clear한 사용자의 수와 fail한 사용자의 수를 각각 clear, fail 리스트로 관리
결과를 [스테이지 번호, 실패율]로 저장 후 실패율에 대해 내림차순, 스테이지 번호에 대해 오름차순으로 정렬 후 스테이지 번호만 리턴

"""

from collections import Counter

def solution(N, stages):
    counter = Counter(stages)

    clear, fail = [0] * (N + 1), [0] * (N + 1)
    for stage, count in counter.items():
        for i in range(stage):
            clear[i] += count
        fail[stage-1] += count

    res = []
    for i in range(N):
        percentage = fail[i] / clear[i] if clear[i] != 0 else 0
        res.append([i+1, percentage])
    return list(map(lambda x: x[0], sorted(res, key = lambda x: (-x[1], x[0]))))