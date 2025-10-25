"""

더 맵게 : https://school.programmers.co.kr/learn/courses/30/lessons/42626

음식의 스코빌 지수가 주어졌을 때, 모든 음식을 원하는 스코빌 지수 이상으로 만들기 위해 섞어야 하는 최소 횟수를 구하는 문제
- 스코빌 지수가 가장 낮은 두 개의 음식을 다음 방법으로 섞어 새로운 음식을 만든다
    - 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
- 음식의 스코빌 지수를 담은 배열 scoville의 길이는 2 이상 1,000,000 이하이다
    - scoville의 원소는 각각 0 이상 1,000,000 이하이다
- 원하는 스코빌 지수 K는 0 이상 1,000,000,000 이하이다
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1을 리턴한다

Example:
- Input : scoville=[1, 2, 3, 9, 10, 12], K=7
- Output : 2

Note:
스코빌 지수가 가장 낮은 음식과 두 번째로 낮은 음식을 빠르게 확인하기 위해 최소힙 사용
heap의 길이가 2보다 작으면 음식 두 가지를 섞을 수 없으므로, 마지막 남은 원소의 값이 K보다 작다면 -1을 리턴

"""

import heapq

def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)
    answer = 0

    while len(heap) >= 2:
        if heap[0] >= K:
            return answer

        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + b * 2)
        answer += 1

    return answer if heap[0] >= K else -1