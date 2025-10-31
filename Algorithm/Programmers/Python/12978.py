"""

배달 : https://school.programmers.co.kr/learn/courses/30/lessons/12978

N개의 마을로 이루어진 나라의 도로 정보가 주어졌을 때, 1번 마을에서 K 시간 내에 도달 가능한 마을의 개수를 구하는 문제
- 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있다
- 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있으며, 도로를 지날 때 걸리는 시간은 도로별로 다르다
- 마을의 개수 N은 1 이상 50 이하의 자연수이다
- 각 마을을 연결하는 도로의 정보 road의 길이는 1 이상 2,000 이하이다
    - road의 각 원소는 길이 3인 배열이며, 순서대로 (a, b, c)를 나타낸다
        - 도로가 연결하는 두 마을의 번호 a, b는 1 이상 N 이하이며, a와 b는 같지 않다
        - 도로를 지나는 데 걸리는 시간 c는 1 이상 10,000 이하의 자연수이다
        - 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있다
        - 한 도로의 정보가 여러 번 중복해서 주어지지 않는다
- K는 1 이상 500,000 이하이다
- 임의의 두 마을 간에 항상 이동 가능한 경로가 존재한다

Example:
- Input : N=5, road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], K=3
- Output : 4
- 1, 2, 4, 5번 마을까지 3 이하의 시간에 도달 가능

- Input : N=6, road=[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], K=4
- Output : 4
- 1, 2, 3, 5번 마을까지 4 이하의 시간에 도달 가능

Note:
dijkstra 알고리즘을 사용하여 해결

"""

import heapq

def solution(N, road, K):
    INF = 9999999
    dist = [0, 0] + [INF] * (N-1)
    graph = [[] for _ in range(N+1)]

    for a, b, c in road:
        graph[a].append([c, b])
        graph[b].append([c, a])

    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        d, now = heapq.heappop(heap)
        for g in graph[now]:
            cost = d + g[0]
            if cost < dist[g[1]]:
                dist[g[1]] = cost
                heapq.heappush(heap, (cost, g[1]))

    return len([d for d in dist[1:] if d <= K])