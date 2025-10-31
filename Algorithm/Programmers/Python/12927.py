"""

야근 지수 : https://school.programmers.co.kr/learn/courses/30/lessons/12927

퇴근까지 남은 시간과 각 일에 대한 작업량이 주어졌을 때, 야근 피로도를 최소화한 값을 구하는 문제
- 야근 피로도는 남은 일의 작업량을 제곱하여 더한 값이다
- 퇴근까지 남은 시간 동안 야근 피로도를 최소화하도록 일한다
- 1시간 동안 작업량 1만큼을 처리할 수 있다
- 각 일에 대한 작업량 works는 길이 1 이상 20,000 이하인 배열이다
    - works의 원소는 50,000 이하인 자연수이다
- 남은 시간 n은 1,000,000 이하인 자연수이다

Example:
- Input : works=[4, 3, 3], n=4
- Output : 12
- 4시간 동안 일을 하여 [2, 2, 2]로 만들면 피로도가 12로 최소이다

- Input : works=[2, 1, 2], n=1
- Output : 6
- 1시간 동안 일을 하여 [1, 1, 2]로 만들면 피로도가 6으로 최소이다

- Input : works=[1, 1], n=3
- Output : 0
- 3시간 후 남은 작업량이 없으므로 피로도는 0이다

Note:
heapq를 사용하여 최대 힙을 생성하여 해결
heapq는 기본적으로 최소 힙이므로, 값을 음수로 변경하여 최대 힙으로 사용한다
가장 작업량이 많은 일부터 줄이는 것이 전체 제곱의 합을 최소화하는 방향이므로
최댓값에서 1씩 빼고 힙에 다시 넣는 방법을 n번 반복

"""

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = [-work for work in works]
    heapq.heapify(heap)

    for _ in range(n):
        temp = heapq.heappop(heap)
        heapq.heappush(heap, temp + 1)

    return sum(x ** 2 for x in heap)