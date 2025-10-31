"""

등산코스 정하기 : https://school.programmers.co.kr/learn/courses/30/lessons/118669

출입구, 쉼터, 산봉우리 및 등산로의 정보가 주어졌을 때, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 최소화하는 등산 코스를 구하는 문제
- 등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 바움ㄴ할 때마다 휴식을 취할 수 있다
- 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라고 부른다
- 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 한다
- 등산코스는 처음 출발한 원래의 출입구로 돌아와야 한다
- intensity가 최소가 되는 등산코스에 포함된 산봉우리의 번호와 intensity의 최솟값을 리턴한다
- intensity가 최소가 되는 등산코스가 여러 개라면 산봉우리의 번호가 가장 낮은 등산코스를 선택한다
- paths의 원소는 [i, j, w]의 형태이다
    - i번 지점과 j번 지점을 연결하는 등산로가 있으며, 두 지점 사이를 이동하는 데 w만큼이 걸린다는 뜻이다
    - 서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개이다
- gates는 1 이상 n 이하의 정수가 포함된 길이 1 이상 n 이하의 정수 배열이다
- summits는 1 이상 n 이하의 정수가 포함된 길이 1 이상 n 이하의 정수 배열이다
- 출입구이면서 동시에 산봉우리인 지점은 없다
- gates와 summits에 등장하지 않은 지점은 모두 쉼터이다
- 임의의 두 지점 사이에 이동 가능한 경로가 항상 존재한다

Example:
- Input : n=6, paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], gates=[1, 3], summits=[5]
- Output : [5, 3]
- 1 -> 2 -> 4 -> 5 -> 6 -> 4 -> 2 -> 1 이 intensity가 최소가 되는 등산코스이다

- Input : n=7, paths=[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], gates=[1], summits=[2, 3, 4]
- Output : [3, 4]

- Input : n=7, paths=[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], gates=[3, 7], summits=[1, 5]
- Output : [5, 1]

- Input : n=5, paths=[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], gates=[1, 2], summits=[5]
- Output: [5, 6]

Note:
우선순위 큐를 사용하여 다익스트라 알고리즘을 변형하여 구현
출입구에서 각 지점까지의 최소 intensity를 visited에 저장
intensity가 최소가 되도록 산봉우리에 도착한다면, 내려갈 때 똑같은 루트로 내려가면 된다
시간 초과 문제를 해결하기 위해 set_summits를 이용

"""

from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    path = defaultdict(list)
    for i, j, w in paths:
        path[i].append((j, w));
        path[j].append((i, w));

    pq = []
    visited = [10000001] * (n + 1)
    summits.sort()
    set_summits = set(summits)

    for g in gates:
        heappush(pq, (0, g))
        visited[g] = 0

    while pq:
        intensity, curr = heappop(pq)

        if curr in set_summits or visited[curr] < intensity:
            continue

        for j, w in path[curr]:
            temp = max(intensity, w)
            if temp < visited[j]:
                visited[j] = temp
                heappush(pq, (temp, j))

    result = [0, 10000001]
    for summit in summits:
        if visited[summit] < result[1]:
            result[0] = summit
            result[1] = visited[summit]

    return result