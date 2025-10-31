"""

징검다리 건너기 : https://school.programmers.co.kr/learn/courses/30/lessons/64062

징검다리 디딤돌에 적힌 숫자가 담긴 배열과 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수가 주어질 때, 최대 몇 명까지 징검다리를 건널 수 있는지 구하는 문제
- 징검다리는 일렬로 놓여 있고, 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며, 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어든다
- 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며, 이 경우 그 다음 디딤돌로 한 번에 여러 칸을 건너뛸 수 있다
- 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건널 수 있다
- 한 번에 한 명씩 징검다리를 건너야 하며, 한 명이 모두 건넌 후에 다음 사람이 건너기 시작한다
- 징검다리를 건너야 하는 사람의 수는 무제한이라고 간주한다
- stones 배열은 크기 1 이상 200,000 이하인 정수 배열로, 각 원소들의 값은 1 이상 200,000,000 이하이다
- k는 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수이며, 1 이상 stones 길이 이하인 자연수이다

Example:
- Input : stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], k=3
- Output : 3

Note:
효율성 테스트에 통과하기 위해 이진 탐색으로 해결
x명의 사람이 건넌다고 했을 때, (디딤돌 숫자 - x)가 0보다 작아지는 연속된 길이가 k 이상이라면 x명의 사람은 건널 수 없다

"""

def solution(stones, k):
    start, end = 1, max(stones)

    while start <= end:
        count = 0
        mid = (start + end) // 2

        for stone in stones:
            if (stone - mid) <= 0:
                count += 1
                if count >= k:
                    break
            else:
                count = 0

        if count >= k:
            end = mid - 1
        else:
            start = mid + 1

    return start
