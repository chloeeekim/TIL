"""

택배 배달과 수거하기 : https://school.programmers.co.kr/learn/courses/30/lessons/150369

일렬로 나열된 n개의 집과 배달할 물건, 수거할 상자들이 주어졌을 때, 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리를 구하는 문제
- 배달할 택배들은 모두 물류창고에 보관되어 있다
- i번째 집은 물류창고에서 거리 i만큼 떨어져 있다
- 트럭에는 최대 cap개의 상자를 실을 수 있다
- 각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있다
- 트럭의 초기 위치는 물류창고이다

Example:
- Input : cap=4, n=5, deliveries=[1, 0, 3, 1, 2], pickups=[0, 3, 0, 4, 0]
- Output : 16

- Input : cap=2, n=7, deliveries=[1, 0, 2, 0, 1, 0, 2], pickups=[0, 2, 0, 1, 0, 2, 0]
- Output : 30

Note:
가장 먼 곳부터 배달하며, 배달하거나 수거할 상자가 하나라도 있다면 해당 집에 도착해야 한다
특정 집에 배달을 갔다면 다시 물류창고로 돌아와야 하기 때문에 거리는 왕복으로 계산

"""

def solution(cap, n, deliveries, pickups):
    total = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    d, p = 0, 0

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            total += (n - i) * 2

    return total
