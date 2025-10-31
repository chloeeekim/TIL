"""

부대복귀 : https://school.programmers.co.kr/learn/courses/30/lessons/132266

지도의 정보와 각 부대원이 위치한 지역들, 강철부대의 지역이 주어졌을 때, 각 부대원들이 강철부대로 복귀할 수 있는 최단시간을 구하는 문제
- 각 지역은 유일한 번호로 구분된다
- 두 지역 간의 길을 통과하는 데 걸리는 시간은 모두 1로 동일하다
- 총 지역의 수 n은 3 이상 100,000 이하의 정수이며, 각 지역은 1부터 n까지의 번호로 구분된다
- 두 지역을 왕복할 수 있는 길 정보를 담은 2차원 정수 배열 roads의 길이는 2 이상 500,000 이하이다
    - roads의 원소는 [a, b] 형태로 두 지역 a, b가 서로 왕복할 수 있음을 의미한다 (1 <= a, b <= n, a != b)
    - 동일한 정보가 중복해서 주어지지 않는다
        - 동일한 [a, b]가 중복해서 주어지지 않는다
        - [a, b]가 있다면 [b, a]는 주어지지 않는다
- 각 부대원이 위치한 서로 다른 지역들을 나타내는 정수 배열 sources의 길이는 1 이상 500 이하이다
    - sources의 원소는 1 이상 n 이하이다
- 강철부대의 지역 destination은 1 이상 n 이하의 정수이다
- 주어진 sources의 원소 순서대로 강철부대로 복귀할 수 있는 최단시간을 담은 배열을 리턴한다
    - 복귀가 불가능한 경우 해당 부대원의 최단 시간은 -1이다

Example:
- Input : n=3, roads=[[1, 2], [2, 3]], sources=[2, 3], destination=1
- Output : [1, 2]

- Input : n=5, roads=[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], sources=[1, 3, 5], destination=5
- Output : [2, -1, 0]

Note:
queue를 이용하여 BFS 방식으로 해결
길은 양방향으로 연결되어 있으므로, 각 부대원들에서 시작하는 거리를 계산하지 않고, 도착지점에서부터 부대원까지의 최단거리를 구한다

"""

from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    roadmap = defaultdict(list)
    for a, b in roads:
        roadmap[a].append(b)
        roadmap[b].append(a)

    dist = [-1] * (n+1)
    dist[destination] = 0

    visited = {destination}
    queue = deque([(destination, 0)])
    while queue:
        area, d = queue.popleft()
        dist[area] = d
        for anext in roadmap[area]:
            if anext not in visited:
                visited.add(anext)
                queue.append((anext, d+1))

    return [dist[x] for x in sources]