"""

[PCCP 기출문제] 2번 / 퍼즐 게임 챌린지 : https://school.programmers.co.kr/learn/courses/30/lessons/340212

퍼즐의 난이도와 소요 시간이 주어졌을 때, 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하는 문제
- 난이도가 숙련도보다 낮거나 같은 경우, 퍼즐을 틀리지 않고 해당 퍼즐의 소요 시간만큼 사용하여 해결한다
- 난이도가 숙련도보다 높은 경우, 난이도와 숙련도의 차이만큼 이전 퍼즐도 다시 풀어야 한다
- 퍼즐은 주어진 순서대로 해결해야 한다
- 첫 번째 퍼즐의 난이도(diffs[0])는 1이다
- 제한 시간 내에 퍼즐을 모두 해결할 수 있는 경우만 입력으로 주어진다

Example:
- Input : diffs=[1,5,3], times=[2,4,7], limit=30
- Output : 3

- Input : diffs=[1,4,4,2], times=[6,3,8,2], limit=59
- Output : 2

- Input : diffs=[1,328,467,209,54], times=[2,7,1,4,3], limit=1723
- Output : 294

- Input : diffs=[1,99999,100000,99995], times=[9999,9001,9999,9001], limit=3567890012
- Output : 39354

Note:
가능한 숙련도의 범위는 최소 1, 최대 max(diffs)
퍼즐의 개수가 최대 300,000개가 주어지기 때문에 순차적으로 확인하는 방법은 매우 비효율적
이진 탐색을 사용하여 해결

"""

def solution(diffs, times, limit):
    low, high = 1, max(diffs)

    while low < high:
        mid = (low + high) // 2

        if can_solve(diffs, mid, times, limit):
            high = mid
        else:
            low = mid + 1
    return high

def can_solve(diffs, level, times, limit):
    total = 0
    for i, diff in enumerate(diffs):
        if diff <= level:
            total += times[i]
        else:
            total += (times[i] + (times[i] + times[i-1]) * (diff - level))
        if total > limit:
            return False
    return True